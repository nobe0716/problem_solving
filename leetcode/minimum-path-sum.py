class Solution:
    def minPathSum(self, grid):
        n, m = len(grid), len(grid[0])
        if n == 0 or m == 0:
            return 0
        t = [[float('inf')] * m for _ in range(n)]
        t[0][0] = grid[0][0]
        for i in range(1, n):
            t[i][0] = t[i - 1][0] + grid[i][0]
        for i in range(1, m):
            t[0][i] = t[0][i - 1] + grid[0][i]

        for i in range(1, n):
            for j in range(1, m):
                t[i][j] = grid[i][j] + min(t[i][j - 1], t[i - 1][j])
        return t[n - 1][m - 1]