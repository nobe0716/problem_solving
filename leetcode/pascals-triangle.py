class Solution(object):
	def generate(self, numRows):
		if numRows == 0:
			return []
		r = [[1]]
		for i in range(1, numRows):
			v = []
			for j in range(i + 1):
				if j == 0 or j == i:
					v.append(1)
				else:
					v.append(r[i - 1][j - 1] + r[i - 1][j])
			r.append(v)
		return r