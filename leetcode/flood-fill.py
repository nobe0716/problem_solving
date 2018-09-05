class Solution:
	def floodFill(self, image, sr, sc, newColor):
		n, m, o = len(image), len(image[0]), image[sr][sc]
		def ff(r, c):
			if not (0 <= r < n and 0 <= c < m) or image[r][c] != o or image[r][c] == newColor:
				return
			#print(r, c)
			image[r][c] = newColor
			ff(r - 1, c)
			ff(r + 1, c)
			ff(r, c - 1)
			ff(r, c + 1)
		ff(sr, sc)
		return image