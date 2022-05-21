from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        MAX_VAL = 10 ** 8
        gr = defaultdict(set)
        gb = defaultdict(set)
        for a, b in redEdges:
            gr[a].add(b)
        for a, b in blueEdges:
            gb[a].add(b)

        tr = [MAX_VAL] * n
        tb = [MAX_VAL] * n
        tr[0] = tb[0] = 0
        vr = set()
        vb = set()
        q = deque()
        for e in gr[0]:
            if e == 0:
                continue
            tr[e] = 1
            q.append((e, 1, True))
        for e in gb[0]:
            if e == 0:
                continue
            tb[e] = 1
            q.append((e, 1, False))

        while q:
            pos, cost, from_red = q.popleft()

            graph, visited, table = (gb, vb, tb) if from_red else (gr, vr, tr)
            for e in graph[pos]:
                if e in visited:
                    continue
                if cost + 1 < table[e]:
                    visited.add(e)
                    table[e] = cost + 1
                    q.append((e, cost + 1, not from_red))

        return [min(a, b) if min(a, b) != MAX_VAL else -1 for a, b in zip(tr, tb)]


s = Solution()
assert s.shortestAlternatingPaths(5, [[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]], [[1,3],[0,0],[0,3],[4,2],[1,0]]) == [0,1,2,1,1]
assert s.shortestAlternatingPaths(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[1, 2], [2, 3], [3, 1]]) == [0, 1, 2, 3, 7]
