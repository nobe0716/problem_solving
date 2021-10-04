# https://codeforces.com/problemset/problem/1526/C1
import heapq
import sys
from typing import List

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline

n = int(input())
potions = [int(x) for x in input().strip().split()]


def solve(n: int, potions: List[int]) -> int:
    health = 0
    h = []
    ans = 0
    for e in potions:
        health += e
        heapq.heappush(h, e)
        while health < 0:
            v = heapq.heappop(h)
            health -= v
    ans = max(ans, len(h))
    return ans


ans = solve(n, potions)
print(ans)
