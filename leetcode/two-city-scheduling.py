from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])
        res = sum(c[0] for c in costs[:n]) + sum(c[1] for c in costs[n:])
        return res


s = Solution()
assert s.twoCitySchedCost(costs=[[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]) == 1859
assert s.twoCitySchedCost(costs=[[10, 20], [30, 200], [400, 50], [30, 20]]) == 110
assert s.twoCitySchedCost(costs=[[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]) == 3086
