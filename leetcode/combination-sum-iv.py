class Solution(object):
    def combinationSum4(self, nums, target):
        if len(nums) == 0:
            return 0
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        t = [1] + [0] * target
        for i in range(min(nums), target + 1):
            t[i] = sum(t[i - j] if i >= j else 0 for j in nums)
        # print(t)
        return t[target]
