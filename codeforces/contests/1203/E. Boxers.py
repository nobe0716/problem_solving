# https://codeforces.com/problemset/problem/1203/E
import sys
from typing import List

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n: int, a: List[int]) -> int:
    a = sorted(a)
    ns = set()
    for e in a:
        if e > 1 and e - 1 not in ns:
            ns.add(e - 1)
        elif e not in ns:
            ns.add(e)
        elif e + 1 not in ns:
            ns.add(e + 1)
    # print(ns)
    return len(ns)


n = int(input())
a = list(map(int, input().split()))

ans = solve(n, a)
print(ans)
