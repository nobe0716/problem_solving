# https://codeforces.com/problemset/problem/778/A

import sys
from typing import List

input = sys.stdin.readline


def solve(t: str, p: str, a: List[int]) -> int:
    def verify(pivot: int) -> bool:
        pass
        j = 0
        a_set = set(a[:pivot])
        for i in range(lt):
            if t[i] == p[j] and i not in a_set:
                j += 1
                if j == lp:
                    return True
        return False

    a = [e - 1 for e in a]
    lt, lp = len(t), len(p)
    lo, hi = 0, len(a)
    r = None
    while lo <= hi:
        pivot = (lo + hi) // 2
        if verify(pivot):
            r = pivot
            lo = pivot + 1
        else:
            hi = pivot - 1

    return r


t = input().strip()
p = input().strip()
a = list(map(int, input().strip().split()))

r = solve(t, p, a)
print(r)
