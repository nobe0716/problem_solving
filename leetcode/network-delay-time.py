import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = defaultdict(dict)
        for u, v, w in times:
            g[u][v] = w

        table = [0] * (N + 1)
        heap = []
        for i in range(1, N + 1):
            if i == K:
                continue
            if i in g[K]:
                table[i] = g[K][i]
                heapq.heappush(heap, (table[i], i))
            else:
                table[i] = float('inf')

        while heap:
            c, u = heapq.heappop(heap)

            for v, w in g[u].items():
                if table[v] > table[u] + w:
                    table[v] = table[u] + w
                    heapq.heappush(heap, (table[v], v))

        return max(table) if max(table) != float('inf') else -1


s = Solution()
assert s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], N=4, K=2) == 2
