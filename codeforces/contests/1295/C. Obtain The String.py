import bisect
from collections import defaultdict


def solve(s, t):
    if set(t) - set(s):
        return -1

    pos = defaultdict(list)
    for i in range(len(s)):
        pos[s[i]].append(i)

    c = 1
    j = pos[t[0]][0]
    for e in t[1:]:
        k = bisect.bisect(pos[e], j)
        if k < len(pos[e]):
            j = pos[e][k]
        else:
            c += 1
            j = pos[e][0]
    return c


for _ in range(int(input())):
    s, t = input(), input()
    print(solve(s, t))
