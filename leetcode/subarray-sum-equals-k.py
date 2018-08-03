from collections import defaultdict


class Solution(object):
	def subarraySum(self, nums, k):
		D = lambda: defaultdict(lambda: 0)

		d = D()
		d[0] = 1
		r = s = 0
		for n in nums:
			s += n
			if s - k in d:
				r += d[s - k]
			d[s] = d[s] + 1
		return r