# 2022-02-20 14:08:38.029565
# https://codeforces.com/problemset/problem/812/C
import heapq
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def proc(n, S, a):
    def find_minimum_cost(k):
        heap = []
        for i in range(k):
            heapq.heappush(heap, -(a[i] + (i + 1) * k))

        for i in range(k, n):
            v = -(a[i] + (i + 1) * k)
            if v < heap[0]:
                continue
            heapq.heappop(heap)
            heapq.heappush(heap, v)
        return -1 * sum(heap)

    lo, hi = 1, n

    max_k, max_t = 0, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cost = find_minimum_cost(mid)
        if cost <= S:
            max_k = mid
            max_t = cost
            lo = mid + 1
        else:
            hi = mid - 1
    return max_k, max_t


n, S = map(int, input().split())
a = list(map(int, input().split()))
ans = proc(n, S, a)
print(*ans)
