from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = t = nums[0]
        for e in nums[1:]:
            t = max(e, t + e)
            r = max(r, t)
        return r