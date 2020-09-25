from collections import defaultdict
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        new_arr = [arr[0], arr[1]]
        for e in arr[2:]:
            if e != new_arr[-1] or e != new_arr[-2]:
                new_arr.append(e)
        arr = new_arr

        n = len(arr)
        positions = defaultdict(set)

        for i in range(n):
            positions[arr[i]].add(i)

        position_to_cost = {0: 0}  # cost to reach that position
        q = {0}
        cost = 0
        while q and (n - 1) not in position_to_cost:
            nq = set()

            for p in q:
                if p - 1 >= 0 and p - 1 not in position_to_cost:
                    position_to_cost[p - 1] = cost + 1
                    nq.add(p - 1)
                if p + 1 < n and p + 1 not in position_to_cost:
                    position_to_cost[p + 1] = cost + 1
                    nq.add(p + 1)
                for pos in positions[arr[p]]:
                    if pos not in position_to_cost:
                        position_to_cost[pos] = cost + 1
                        nq.add(pos)
            cost += 1
            q = nq

        return position_to_cost[n - 1]


s = Solution()
assert s.minJumps([7]) == 0
assert s.minJumps([7, 7]) == 1
assert s.minJumps([7] * (5 * 10 ^ 4)) == 1
assert s.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]) == 3
