# https://codeforces.com/contest/1372/problem/C
import sys
from typing import List

input = sys.stdin.readline


def solve(n: int, a: List[int]) -> int:
    lo = 0
    while lo < n and a[lo] == lo + 1:
        lo += 1
    hi = n - 1
    while hi >= 0 and a[hi] == hi + 1:
        hi -= 1

    if lo == n:
        return 0

    for i in range(lo, hi):
        if a[i] == i + 1:
            return 2

    return 1


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    r = solve(n, a)
    print(r)
