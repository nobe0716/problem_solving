class Solution(object):
	def numIslands(self, grid):
		def coloring(grid, n, m, i, j, c):
			if 0 <= i < n and 0 <= j < m and grid[i][j] == '1':
				grid[i][j] = c
				coloring(grid, n, m, i - 1, j, c)
				coloring(grid, n, m, i + 1, j, c)
				coloring(grid, n, m, i, j - 1, c)
				coloring(grid, n, m, i, j + 1, c)

		if len(grid) == 0:
			return 0
		c = 2
		n, m = len(grid), len(grid[0])
		for i in range(n):
			for j in range(m):
				if grid[i][j] == '1':
					coloring(grid, n, m, i, j, c)
					c += 1
		return c - 2