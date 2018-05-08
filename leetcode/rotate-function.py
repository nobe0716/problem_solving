'''
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (1 * 4) + (2 * 3) + (3 * 2) + (0 * 6) +  = 0 + 4 + 6 + 6 = 16
F(2) = (2 * 4) + (3 * 3) + (0 * 2) + (1 * 6) +  = 0 + 6 + 8 + 9 = 23
F(3) = (3 * 4) + (0 * 3) + (1 * 2) + (2 * 6) +  = 0 + 2 + 12 + 12 = 26
'''
class Solution(object):
    def maxRotateFunction(self, A):
        m = v = sum(map(lambda x: x[0] * x[1], enumerate(A)))
        s = sum(A)
        for i in range(len(A) - 1, 0, -1):
            v += (s - len(A) * A[i])
            m = max(m, v)
        return m

s = Solution()
print (s.maxRotateFunction([4, 3, 2, 6]))