from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = nums.copy()
        l = len(nums)
        p = 1
        for i in range(l - 2, 0, -1):
            r[i] = r[i] * r[i + 1]
        for i in range(0, l - 1):
            p, r[i] = p * nums[i], p * r[i + 1]
        r[-1] = p
        return r


s = Solution()
assert (s.productExceptSelf([1, 0])) == [0, 1]
assert (s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
