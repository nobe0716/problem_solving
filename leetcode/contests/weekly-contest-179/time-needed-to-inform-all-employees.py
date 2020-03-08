import heapq
from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(dict)
        h = []
        for i, m in enumerate(manager):
            g[m][i] = informTime[m]

        visited = set([headID])
        costs = [float('inf')] * n
        costs[headID] = 0

        id = headID
        for k, v in g[id].items():
            heapq.heappush(h, (v, k))
            costs[k] = v

        visited.add(id)

        while h:
            cost, id = heapq.heappop(h)
            if id in visited:
                continue
            visited.add(id)

            for k, v in g[id].items():
                if cost + v < costs[k]:
                    costs[k] = cost + v
                    heapq.heappush(h, (cost + v, k))

        return max(costs)


s = Solution()
assert s.numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]) == 1
assert s.numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]) == 0
assert s.numOfMinutes(n=7, headID=6, manager=[1, 2, 3, 4, 5, 6, -1], informTime=[0, 6, 5, 4, 3, 2, 1]) == 21
assert s.numOfMinutes(n=15, headID=0, manager=[-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                      informTime=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]) == 3
assert s.numOfMinutes(n=4, headID=2, manager=[3, 3, -1, 2], informTime=[0, 0, 162, 914]) == 1076
