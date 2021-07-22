# https://codeforces.com/problemset/problem/1526/C2
import heapq
import sys

n = int(input())
a = [int(x) for x in sys.stdin.readline().strip().split()]
h = []  # heap

p = 0  # health point
s = 0  # skip count
for e in a:
    if e >= 0:
        p += e
        continue

    while h and h[0] < e and p + e < 0:
        p -= heapq.heappop(h)
        s += 1

    if p + e < 0:
        s += 1
    else:
        p += e
        heapq.heappush(h, e)

print(n - s)
