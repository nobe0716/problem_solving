class Solution:
	def findAndReplacePattern(self, words, pattern):
		def matches(w, p):
			if len(w) != len(p):
				return False
			d, e = {}, {}
			for a, b in zip(w, p):
				if a in d and b in e:
					if d[a] != b or e[b] != a:
						return False
				elif a in d or b in e:
					return False
				else:
					d[a] = b
					e[b] = a
			return True

		r = []
		for w in words:
			if matches(w, pattern):
				r.append(w)
		return r