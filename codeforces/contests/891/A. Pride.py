# 2022-08-15 23:07:59.884729
# https://codeforces.com/problemset/problem/891/A
from collections import Counter
from functools import reduce
from math import gcd
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, a):
    if all(e == 1 for e in a):
        return 0
    if any(e == 1 for e in a):
        return n - Counter(a)[1]
    if reduce(lambda x, y: gcd(x, y), a) > 1:
        return -1

    c = n
    while True:
        b = []
        for i in range(len(a) - 1):
            g = gcd(a[i], a[i + 1])
            b.append(g)
            if g == 1:
                return c
        a = b
        c += 1

    return c


n = int(input().strip())
a = list(map(int, input().strip().split()))
print(proc(n, a))
