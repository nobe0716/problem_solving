# https://codeforces.com/contest/1389/problem/C
import sys
from collections import Counter

from string import digits

sys.setrecursionlimit(200_000)


def solve(s):
    c = Counter(s)
    n = len(s)

    candidates = []
    for i in digits:
        candidates.append(n - c[i])

    for i in digits:
        for j in digits:
            if i == j:
                continue
            token = i + j
            idx = 0
            remove_count = 0
            for k in s:
                if token[idx] != k:
                    remove_count += 1
                else:
                    idx = (idx + 1) % 2

            candidates.append(remove_count + idx)
    return min(candidates)


# assert solve('123456789' * 20000) > 0
# assert solve('95831') == 3
# assert solve('100120013') == 5
# assert solve('252525252525') == 0
# assert solve('0135785152174082012097654604938957981703096740171424318330885652765893707675593434217828455171007143914259658511312169208710262035594955071894747649') == 124
for _ in range(int(input())):
    s = input()
    r = solve(s)
    print(r)
