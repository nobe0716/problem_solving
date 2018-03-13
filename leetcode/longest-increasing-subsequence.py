class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) < 1:
            return 0
        t = [0] * len(nums)
        t[0] = 1
        for i in range(1, len(nums)):
            v = 0
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if t[j] > v:
                    v = t[j]
            t[i] = v + 1
        return max(t)