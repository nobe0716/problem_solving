# https://codeforces.com/contest/1475/problem/E
import math
import sys
from collections import Counter

input = sys.stdin.readline

_MOD = 10 ** 9 + 7


def solve(n, k, a):
    c = Counter(a)
    for key in sorted(c.keys(), reverse=True):
        num = c[key]
        if k >= num:
            k -= num
        else:
            # num_C_k
            r = 1
            return math.comb(num, k) % _MOD
    return 1


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    r = solve(n, k, a)
    print(r)
