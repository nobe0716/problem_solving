from collections import defaultdict
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        n = len(routes)
        bus_stop_sets = []

        t = {}
        start_pos = set()
        end_pos = set()
        for i, route in enumerate(routes):
            but_stop_set = set(route)
            bus_stop_sets.append(but_stop_set)
            if S in but_stop_set:
                start_pos.add(i)
                t[i] = 1
            if T in but_stop_set:
                end_pos.add(i)

        g = defaultdict(set)
        for i in range(n - 1):
            for j in range(1, n):
                if bus_stop_sets[i] & bus_stop_sets[j]:
                    g[i].add(j)
                    g[j].add(i)

        if start_pos & end_pos:
            return 1

        depth = 1
        q = start_pos
        while q:
            nq = set()
            for e in q:
                if e in end_pos:
                    return depth
                for next in g[e]:
                    if next in t:
                        continue
                    nq.add(next)
                    t[next] = depth + 1

            depth += 1
            q = nq
        return -1


s = Solution()
assert s.numBusesToDestination(
    [[25, 33], [3, 5, 13, 22, 23, 29, 37, 45, 49], [15, 16, 41, 47], [5, 11, 17, 23, 33], [10, 11, 12, 29, 30, 39, 45],
     [2, 5, 23, 24, 33], [1, 2, 9, 19, 20, 21, 23, 32, 34, 44], [7, 18, 23, 24], [1, 2, 7, 27, 36, 44], [7, 14, 33]], 7,
    47)
