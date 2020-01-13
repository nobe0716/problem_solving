from collections import defaultdict
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        g = defaultdict(set)
        for i, j in connections:
            g[i].add(j)
            g[j].add(i)

        visited = set()

        def dfs(i):
            if i in visited:
                return 0
            visited.add(i)
            for j in g[i]:
                dfs(j)
            return 1

        # return solve_using_disjoint_set(n, connections)
        return sum(dfs(i) for i in range(n)) - 1


s = Solution()
assert (s.makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]])) == 1
assert (s.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]])) == 2
assert (s.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]])) == -1
assert (s.makeConnected(n=5, connections=[[0, 1], [0, 2], [3, 4], [2, 3]])) == 0
