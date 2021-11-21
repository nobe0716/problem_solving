# https://www.acmicpc.net/problem/2357
import math
import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input().strip()))

BASE = 2 ** math.ceil(math.log2(n))

sa_min = [float('inf')] * BASE + a
sa_max = [float('-inf')] * BASE + a
# sa = [(float('inf'), float('-inf'))]

for i in range(BASE, BASE + n):
    p = i
    while p // 2 > 0:
        sa_min[p // 2] = min(sa_min[p // 2], sa_min[p])
        sa_max[p // 2] = max(sa_max[p // 2], sa_max[p])
        p //= 2


def get_min(a, b):
    if a == b:
        return sa_min[a]
    elif a > b:
        return float('inf')

    candidates = []
    if a % 2 == 1:
        candidates.append(sa_min[a])
        a += 1
    if b % 2 == 0:
        candidates.append(sa_min[b])
        b -= 1

    return min(get_min(a // 2, b // 2), min(candidates) if candidates else float('inf'))


def get_max(a, b):
    if a == b:
        return sa_max[a]
    elif a > b:
        return float('-inf')

    candidates = []
    if a % 2 == 1:
        candidates.append(sa_max[a])
        a += 1
    if b % 2 == 0:
        candidates.append(sa_max[b])
        b -= 1

    return max(get_max(a // 2, b // 2), max(candidates) if candidates else float('-inf'))


for _ in range(m):
    a, b = map(int, input().split())
    a += BASE - 1
    b += BASE - 1
    imin = get_min(a, b)
    imax = get_max(a, b)
    print(imin, imax)
