class Solution(object):
    def findKthNumber(self, n, k):
        if k < 10:
            return k

        return None

s = Solution()
n = 13
k = 2
print(s.findKthNumber(n, k))