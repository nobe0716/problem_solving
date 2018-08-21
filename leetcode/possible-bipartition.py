from collections import defaultdict

class Solution:

	def possibleBipartition(self, N, dislikes):
		g = defaultdict(set)
		for a, b in dislikes:
			g[a].add(b)
			g[b].add(a)
		color_book = {}

		for i in range(1, N + 1):
			if i not in color_book:
				color_book[i] = True
			s = [i]
			while len(s) > 0:
				v = s.pop()
				c = color_book[v]
				for n in g[v]:
					if n not in color_book:
						color_book[n] = not c
						s.append(n)
					elif color_book[n] == c:
						return False
		return True