from typing import List

from sortedcontainers import SortedDict


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        elements = list(zip(startTime, endTime, profit))
        elements.sort(key=lambda x: (x[1], x[0], x[2]))
        t = SortedDict()
        t[elements[0][1]] = elements[0][2]
        max_profit = elements[0][2]
        for start, end, profit in elements[1:]:
            idx = t.bisect(start)
            if idx == 0:
                new_profit = profit
            elif idx == len(t):
                new_profit = max_profit + profit
            else:
                keys = t.keys()
                last_key = keys[idx - 1]
                new_profit = t[last_key] + profit

            if new_profit > max_profit:
                max_profit = new_profit
                t[end] = max_profit

        return max_profit


s = Solution()
assert s.jobScheduling([6, 15, 7, 11, 1, 3, 16, 2], [19, 18, 19, 16, 10, 8, 19, 8], [2, 9, 1, 19, 5, 7, 3, 19]) == 41
# assert s.jobScheduling(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]) == 120
# assert s.jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]) == 6
