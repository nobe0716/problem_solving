# python 2.7
class Solution:
    def largestNumber(self, nums):
        def cmp_str(a, b):
            return cmp(a + b, b + a)
        nums_as_str = sorted(map(str, nums), cmp=cmp_str, reverse=True)
        i = 0
        while i < len(nums_as_str) - 1 and nums_as_str[i] == '0':
            i += 1
        return "".join(nums_as_str[i:])