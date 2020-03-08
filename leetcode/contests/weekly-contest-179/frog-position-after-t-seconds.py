from collections import defaultdict
from typing import List


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        visited = set([1])
        q = [(1.0, 1)]
        turn = 0
        while q and turn < t:
            nq = []
            for prob, vertex in q:
                visited.add(vertex)
                num_of_nodes = sum(1 if e not in visited else 0 for e in g[vertex])
                if num_of_nodes == 0:
                    nq.append((prob, vertex))
                    continue

                for next_vertex in g[vertex]:
                    if next_vertex in visited:
                        continue
                    nq.append((prob / num_of_nodes, next_vertex))
            q = nq
            turn += 1

        for prob, vertex in q:
            if target == vertex:
                return prob
        return 0.0


s = Solution()
print(s.frogPosition(9, [[2, 1], [3, 1], [4, 2], [5, 3], [6, 5], [7, 4], [8, 7], [9, 7]], 1, 8))
print(s.frogPosition(9, [[2, 1], [3, 1], [4, 2], [5, 3], [6, 5], [7, 4], [8, 7], [9, 7]], 1, 8))
print(s.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=2, target=4))
print(s.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=1, target=7))
print(s.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=20, target=6))
print(s.frogPosition(3, [[2, 1], [3, 2]], 1, 2))
print(s.frogPosition(8, [[2, 1], [3, 2], [4, 1], [5, 1], [6, 4], [7, 1], [8, 7]], 7, 7))
print(s.frogPosition(1, [], 1, 1))
