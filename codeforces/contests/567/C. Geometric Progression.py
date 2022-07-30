# 2022-07-30T20:45:49Z
from collections import Counter


def proc(n, k, a):
    c0 = Counter()
    c1 = Counter()
    c2 = Counter()

    for e in a:
        if e % k == 0:
            if (e // k) in c1:
                c2[e] += c1[e // k]
            if (e // k) in c0:
                c1[e] += c0[e // k]
        c0[e] += 1
    return sum(c2.values())


n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = proc(n, k, a)
print(ans)