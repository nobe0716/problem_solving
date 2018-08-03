class Solution(object):
	def countSubstrings(self, s):
		r, l = 0, len(s)
		for a, b in [(x, x) for x in range(l)] + [(x, x + 1) for x in range(l - 1)]:
			while 0 <= a and b < l and s[a] == s[b]:
				r, a, b = r + 1, a - 1, b + 1
		return r