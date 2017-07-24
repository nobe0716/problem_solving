class Solution(object):
    def findErrorNums(self, nums):
        d = {}
        for v in nums:
            d[v] = (0 if (v not in d) else d[v]) + 1

        dup = missing = None
        for i in range(1, len(nums) + 1):
            if i not in d:
                missing = i
            elif d[i] == 2:
                dup = i

        return [dup, missing]


s = Solution()
print s.findErrorNums([1, 2, 2, 4])