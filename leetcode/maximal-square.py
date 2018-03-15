class Solution:
    def rec(self, matrix, n, m, x, y, c):
        if x + c >= n or y + c >= m:
            return c

        for i in range(c):
            if matrix[x + i][y + c] is '0':
                return c
            if matrix[x + c][y + i] is '0':
                return c
        if matrix[x + c][y + c] is '0':
            return c
        return self.rec(matrix, n, m, x, y, c + 1)



    def maximalSquare(self, matrix):
        if len(matrix) is 0:
            return 0
        n, m = len(matrix), len(matrix[0])

        r = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] is "1":
                    r = max(r, self.rec(matrix, n, m, i, j, 1))

        return r * r

s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

