class Solution:
    def singleNumber(self, nums):
        v = 0
        for n in nums:
            v ^= n
        return v

