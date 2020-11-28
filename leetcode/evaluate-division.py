from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(lambda: defaultdict(float))
        for exp, val in zip(equations, values):
            a, b = exp
            g[a][b] = val
            g[b][a] = 1.0 / val

        def inquiry(a, b):
            if a == b and a in g:
                return 1.0
            q = {(a, 1.0)}
            visited = {a}
            while q:
                nq = set()
                for node, value in q:

                    for next_node, next_value in g[node].items():
                        if next_node in visited:
                            continue
                        if next_node == b:
                            return value * next_value
                        visited.add(next_node)
                        nq.add((next_node, value * next_value))
                q = nq
            return None

        res = []
        for a, b in queries:
            result = inquiry(a, b)
            if result:
                res.append(result)
            else:
                res.append(-1.0)
        # print(res)
        return res


s = Solution()
assert s.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                      [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [6.0, 0.5, -1.0, 1.0, -1.0]
