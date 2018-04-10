class Solution:
	def minDistance(self, word1, word2):
		n, m = len(word1), len(word2)
		if n == 0 or m == 0:
			return n + m
		t = [[0] * m for _ in range(n)]

		for i in range(m):
			if word1[0] == word2[i]:
				t[0][i] = 1
			elif i > 0:
				t[0][i] = t[0][i - 1]
		for i in range(n):
			if word1[i] == word2[0]:
				t[i][0] = 1
			elif i > 0:
				t[i][0] = t[i - 1][0]


		for i in range(0, n):
			for j in range(0, m):
				if i == 0 or j == 0:
					#print (t[i][j], end = ' ')
					continue
				if word1[i] == word2[j]:
					t[i][j] = t[i - 1][j - 1] + 1
				else:
					t[i][j] = max(t[i - 1][j], t[i][j - 1])
				#print (t[i][j], end = ' ')
			#print()

		l = max([t[i][j] for j in range(m) for i in range(n)])

		#print ("n, m, l = (%d, %d, %d)" % (n, m, l))
		return n + m - 2 * l