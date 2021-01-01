import bisect
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        a = [0]
        min_sum_len = float('inf')
        for i, e in enumerate(nums):
            a.append(a[-1] + e)

            if a[-1] >= s:
                idx = bisect.bisect_right(a, a[-1] - s)
                min_sum_len = min(min_sum_len, i - idx + 2)
        return min_sum_len if min_sum_len != float('inf') else 0


s = Solution()
assert s.minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]) == 2
