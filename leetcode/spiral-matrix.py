class Solution:
	def spiralOrder(self, matrix):
		x, y = 0, 0
		d = 0
		D = (0, 1), (1, 0), (0, -1), (-1, 0)
		n = len(matrix)
		if n == 0:
			return []
		m = len(matrix[0])
		min_x, max_x, min_y, max_y = 0, n - 1, 0, m - 1

		r = []
		for _ in range(n * m):
			r.append(matrix[x][y])
			x, y = x + D[d][0], y + D[d][1]
			if y > max_y: # d is 0
				x, y = x + 1, y - 1
				d = 1
				min_x += 1
			elif x > max_x: # d is 1
				x, y = x - 1, y - 1
				d = 2
				max_y -= 1
			elif y < min_y: # d is 3
				x, y = x - 1, y + 1
				d = 3
				max_x -= 1
			elif x < min_x:
				x, y = x + 1, y + 1
				d = 0
				min_y += 1
		return r