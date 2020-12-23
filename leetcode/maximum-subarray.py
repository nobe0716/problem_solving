from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        v = nums[0]
        r = nums[0]
        for e in nums[1:]:
            v = v + e if v > 0 else e
            r = max(r, v)
        return r
