import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        li = bisect.bisect_left(nums, target)
        ro = bisect.bisect_right(nums, target)
        if li >= len(nums) or nums[li] != target or ro == 0 or nums[ro - 1] != target:
            return [-1, -1]
        return [li, ro - 1]
