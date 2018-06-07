class Solution(object):
    def arrayPairSum(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        nums = list(sorted(nums))
        v = 0
        for i in range(0, l, 2):
            v += nums[i]
        return v
