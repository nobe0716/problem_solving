from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            while 0 < nums[i] <= l and nums[i] != i + 1:
                e = nums[i]
                if nums[e - 1] == nums[i]:
                    break
                nums[e - 1], nums[i] = nums[i], nums[e - 1]
        for i, e in enumerate(nums):
            if e != i + 1:
                return i + 1
        return l + 1


s = Solution()
assert s.firstMissingPositive([-1, 4, 2, 1, 9, 10]) == 3
assert s.firstMissingPositive(nums=[1, 2, 0]) == 3
assert s.firstMissingPositive(nums=[7, 8, 9, 11, 12]) == 1
assert s.firstMissingPositive(nums=[3, 4, -1, 1]) == 2
assert s.firstMissingPositive(nums=[1, 1]) == 2
assert s.firstMissingPositive(nums=[1, 2]) == 3
