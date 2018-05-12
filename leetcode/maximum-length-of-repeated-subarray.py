class Solution(object):
    def findLength(self, A, B):
        n = len(A)
        m = len(B)
        t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            if A[i] == B[0]:
                t[i][0] = 1
        for i in range(m):
            if A[0] == B[i]:
                t[0][i] = 1
        r = 0
        for i in range(1, n):
            for j in range(1, m):
                if A[i] == B[j]:
                    t[i][j] = t[i - 1][j - 1] + 1
                    r = max(r, t[i][j])

        # for i in range(n):
        #     print(t[i])
        return r


s = Solution()
print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))
# print(s.findLength([1,1,0,0,1], [1,1,0,0,0]))
