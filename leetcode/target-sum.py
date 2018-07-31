from collections import defaultdict

class Solution(object):
	def findTargetSumWays(self, nums, S):
		D = lambda: defaultdict(lambda: 0)
		t = D()
		t[0] = 1
		for n in nums:
			u = D()
			for e in t.keys():
				u[e + n] += t[e]
				u[e - n] += t[e]
			t = u
		return t[S]