class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid):
		if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
			return 0
		n, m = len(obstacleGrid), len(obstacleGrid[0])
		t = [[0 for _ in range(m)] for _ in range(n)]

		t[0][0] = 1 - obstacleGrid[0][0]

		for i in range(0, n):
			for j in range(0, m):
				if obstacleGrid[i][j] == 1:
					continue
				if i + 1 < n and obstacleGrid[i + 1][j] == 0:
					t[i + 1][j] += t[i][j]
				if j + 1 < m and obstacleGrid[i][j + 1] == 0:
					t[i][j + 1] += t[i][j]

		#for i in range(n):
		#    print(t[i])
		return t[n - 1][m - 1]

