from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int) -> int:
            if i < 0:
                return 0
            elif i <= 1:
                return nums[i]
            return max(dp(i - 2), dp(i - 3)) + nums[i]

        return max(dp(len(nums) - 2), dp(len(nums) - 1))


s = Solution()
assert s.rob([1, 2, 3, 1]) == 4
