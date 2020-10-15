import sys
from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        sys.setrecursionlimit(50_000)
        graph_o = defaultdict(set)
        graph_r = defaultdict(set)
        for a, b in connections:
            graph_o[a].add(b)
            graph_r[b].add(a)

        q = deque([0])
        visited = {0}
        r = 0
        while q:
            v = q.popleft()

            for _ in graph_o[v]:
                if _ not in visited:
                    visited.add(_)
                    q.append(_)
                    r += 1
            for _ in graph_r[v]:
                if _ not in visited:
                    visited.add(_)
                    q.append(_)
        return r


s = Solution()
assert s.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
assert s.minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
