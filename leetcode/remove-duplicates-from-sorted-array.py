class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        v = -1
        while i < len(nums):
            if v != nums[i]:
                v = nums[i]
                i += 1
            else:
                nums.pop(i)
        return nums

s = Solution()
print(s.removeDuplicates([]))
print(s.removeDuplicates([1, 1, 2]))
