class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = j = 0

        while i < l or j < l:
            while i < l and nums[i] != 0:
                i += 1
            while j < l and (nums[j] == 0 or j < i):
                j += 1
            if j < l:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
