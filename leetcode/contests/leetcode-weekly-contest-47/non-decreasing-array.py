class Solution(object):
    def checkPossibility(self, nums):
        l = len(nums)
        if l == 0:
            return True
        v = nums[0]
        c = 0
        for i in range(l - 1):
            if nums[i] > nums[i + 1]:
                c += 1
                if i > 0 and nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]
        return c <= 1

s = Solution()
print s.checkPossibility([4,2,3])
print s.checkPossibility([3,4,2,3])