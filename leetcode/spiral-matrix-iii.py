class Solution:
	def spiralMatrixIII(self, R, C, r0, c0):
		VISITED = [[False for _ in range(C)] for _ in range(R)]
		DIRECTION = [0, 1], [1, 0], [0, -1], [-1, 0]

		def in_bound(x, y):
			return 0 <= x < R and 0 <= y < C

		def is_visited(x, y):
			return in_bound(x, y) and VISITED[x][y]

		def get_direction(x, y, d):
			if d == 0:
				if y == C or not is_visited(x + 1, y):
					return 1
				return 0
			elif d == 1:
				if x == R or not is_visited(x, y - 1):
					return 2
				return 1
			elif d == 2:
				if y == -1 or not is_visited(x - 1, y):
					return 3
				return 2
			elif d == 3:
				if x == -1 or not is_visited(x, y + 1):
					return 0
				return 3

		x, y, d = r0, c0, 0
		r = [[x, y]]
		VISITED[x][y] = True

		while len(r) < R * C:
			x += DIRECTION[d][0]
			y += DIRECTION[d][1]
			if in_bound(x, y):
				r.append([x, y])
				VISITED[x][y] = True
			d = get_direction(x, y, d)
		return r


s = Solution()
print(s.spiralMatrixIII(1, 4, 0, 0))
print(s.spiralMatrixIII(5, 6, 1, 4))
