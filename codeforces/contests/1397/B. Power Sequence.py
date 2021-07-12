# https://codeforces.com/contest/1397/problem/B
import sys

_LIMIT = 10 ** 18


def test(n, a, c):
    v = 1
    r = 0
    for i in range(n):
        r += abs(v - a[i])
        v *= c
        if v >= _LIMIT:
            return _LIMIT, v
    return r, v


def solve(n, a):
    a = [int(x) for x in a.strip().split()]
    a = sorted(a)
    r, cn = test(n, a, 1)
    for i in range(1, 10 ** 9):
        v, cn = test(n, a, i)
        if cn > _LIMIT or cn // i > r + a[-1]:
            break
        r = min(r, v)
    return r


# assert solve(3, "1 3 2") == 1
# assert solve(3, "1000000000 1000000000 1000000000") == 1999982505
# assert solve(20, "51261 11877 300 30936722 84 75814681 352366 23 424 16392314 27267 832 4 562873474 33 516967731 158909407 32148531 66 757") == 850575966
input = sys.stdin.readline
n = int(input())
a = input()

r = solve(n, a)
print(r)
