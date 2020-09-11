from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)  # represent manager -> employee
        for i, m in enumerate(manager):
            g[m].append(i)

        def rec(head):
            if head not in g:
                return 0
            return informTime[head] + max(rec(e) for e in g[head])

        return rec(headID)


s = Solution()
assert s.numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]) == 1
assert s.numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]) == 0
assert s.numOfMinutes(n=7, headID=6, manager=[1, 2, 3, 4, 5, 6, -1], informTime=[0, 6, 5, 4, 3, 2, 1]) == 21
assert s.numOfMinutes(n=15, headID=0, manager=[-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                      informTime=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]) == 3
assert s.numOfMinutes(n=4, headID=2, manager=[3, 3, -1, 2], informTime=[0, 0, 162, 914]) == 1076
