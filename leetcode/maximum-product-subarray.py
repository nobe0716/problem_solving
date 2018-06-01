class Solution:
    def maxProduct(self, nums):
        l = len(nums)
        if l == 1:
            return nums[0]
        t = [[nums[0], nums[0]] for _ in range(l)] # 1st; max, 2nd; min
        t[0] = [nums[0], nums[0]]
        for i in range(1, l):
            t[i][0] = max(nums[i], t[i - 1][0] * nums[i], t[i - 1][1] * nums[i])
            t[i][1] = min(nums[i], t[i - 1][0] * nums[i], t[i - 1][1] * nums[i])
        #print(t)
        return max(max(x) for x in t)