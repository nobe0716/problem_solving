# T = O(nlogn), S = O(n)

class Solution(object):
    def findUnsortedSubarray(self, nums):
        # sort given array
        sorted_nums = sorted(nums)
        # find idx l, r
        # l; first index, which nums[l] != sorted_nums[l]
        # r; last index, which nums[r] != sorted_nums[r]
        l = r = None
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if l is None:
                    l = i
                r = i
        return r - l + 1 if l is not None else 0  # return 0 if r is None, nums is already sorted!