from collections import defaultdict
from typing import List, Dict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(lambda: set())
        for i, j in connections:
            g[i].add(j)
            g[j].add(i)

        set_edges_in_cycle = set()

        def dfs(before: int, node: int, stack: List, index_of_node: Dict[int, int]):
            if node in index_of_node:
                for edge in stack[index_of_node[node]:]:
                    set_edges_in_cycle.add(edge)
                return
            index_of_node[node] = len(stack)
            for next in g[node]:
                next_edge = (node, next)
                if next != before:
                    stack.append(next_edge)
                    dfs(node, next, stack, index_of_node)
                    stack.pop()

        dfs(-1, 0, [], {})
        r = []
        for i, j in connections:
            if (i, j) not in set_edges_in_cycle and (j, i) not in set_edges_in_cycle:
                r.append([i, j])
        return r


s = Solution()
assert s.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]) == [[1, 3]]
# assert s.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]) == [[1, 3]]
# print(r)
# assert r
