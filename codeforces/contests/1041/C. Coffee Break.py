# 2022-09-25 11:44:29.026509
# https://codeforces.com/problemset/problem/1041/C
import heapq
import sys
from operator import itemgetter

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write

n, m, d = map(int, input().split())
a = list(map(int, input().split()))

ans = [0] * n
h = []
for i, e in sorted(enumerate(a), key=itemgetter(1)):
    if not h:
        heapq.heappush(h, [e, 1])
        ans[i] = 1
    elif e - h[0][0] >= d + 1:
        v, j = heapq.heappop(h)
        heapq.heappush(h, [e, j])
        ans[i] = j
    else:
        heapq.heappush(h, [e, len(h) + 1])
        ans[i] = len(h)

print(len(h))
print(' '.join(map(str, ans)))
