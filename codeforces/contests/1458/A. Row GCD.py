# https://codeforces.com/contest/1458/problem/A
import math
import sys
from functools import reduce

input = sys.stdin.readline

n, m = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]
b = [int(x) for x in input().strip().split()]

if n == 1:
    r = [e + a[0] for e in b]
else:
    a = sorted(a)
    gcd_a = reduce(lambda g, i: math.gcd(a[i] - a[i - 1], g), range(1, n), a[1] - a[0])

    r = []
    for e in b:
        r.append(math.gcd(a[0] + e, gcd_a))

print(' '.join(map(str, r)))
