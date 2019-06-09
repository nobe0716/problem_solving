"""
## Name of Prob
399. Evaluate Division

## Link
https://leetcode.com/problems/evaluate-division/

## Note

## Input

## Output

## Strategy
Use dfs to find path from a to b
"""

from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(lambda: defaultdict(lambda: 0.0))
        for equation, value in zip(equations, values):
            a, b = equation
            """
            a / b = value
            a = b * value
            b = a / value
            """
            g[a][b] = value
            g[b][a] = 1.0 / value
        res = []

        # want to know a / b = ?
        #   a = b * ?
        def find(g, a, b, visited):
            if a not in g or b not in g:
                return None
            elif a == b:
                return 1.0
            elif b in g[a]:
                return g[a][b]

            for k, v in g[a].items():
                if k in visited:
                    continue
                visited.add(k)

                r = find(g, k, b, visited)
                if r is not None:
                    return v * r * 1.0
            return None

        for query in queries:
            a, b = query
            r = find(g, a, b, set())
            res.append(r if r is not None else -1.0)
        return res


s = Solution()
r = s.calcEquation([["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
                   , [3.0, 4.0, 5.0, 6.0]
                   , [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]])
assert r == [360.0, 0.00833, 20.0, 1.0, -1.0, -1.0]

r = s.calcEquation([["a", "b"], ["b", "c"]]
                   , [2.0, 3.0]
                   , [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
assert r == [6.0, 0.5, -1.0, 1.0, -1.0]
