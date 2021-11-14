# https://codeforces.com/problemset/problem/1379/B
import math
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(l: int, r: int, m: int) -> int:
    def is_feasible(x):
        return l <= x <= r

    n_lo = int(math.ceil((m + l) / r - 1))
    n_hi = int(math.floor((m + r) / l - 1))

    # if n_lo == 0 and 0 <= m <= r - l:
    #     a = l
    #     b = l + m
    #     c = l
    #     return a, b, c
    n = n_lo
    for n in range(max(1, n_lo), n_hi + 1):
        a_lo = int(math.ceil((m - (r - l))) / n)
        a_hi = int(math.ceil((m + (r - l))) / n)
        for a in range(max(l, a_lo), min(r, a_hi) + 1):
            bmc = m - n * a
            if bmc == 0:
                return a, l, l
            elif l - r <= bmc < 0:
                b = l
                c = b - bmc
                return a, b, c
            elif 0 < bmc <= r - l:
                c = l
                b = bmc + c
                return a, b, c
    raise ValueError('invalid condition with {}'.format(n))


# print(solve(10, 12, 43))

for _ in range(int(input())):
    l, r, m = map(int, input().split())
    a, b, c = solve(l, r, m)
    print(a, b, c)
