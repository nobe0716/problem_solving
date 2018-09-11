import math


class NumArray:

	def __init__(self, nums):
		l = len(nums)
		if l == 0:
			return
		self.BASE = int(math.pow(2, math.ceil(math.log(l, 2))))
		self.t = [0] * self.BASE + nums
		l = len(self.t)
		for i in range(self.BASE - 1, 0, -1):
			self.t[i] += self.t[i * 2] if i * 2 < l else 0
			self.t[i] += self.t[i * 2 + 1] if (i * 2 + 1 < l) else 0

	def update(self, i, val):
		idx = self.BASE + i
		delta = val - self.t[idx]
		while idx > 0:
			self.t[idx] += delta
			idx //= 2

	def sumRange(self, i, j):
		s = 0
		i += self.BASE
		j += self.BASE
		while i < j:
			if i % 2 == 1:
				s += self.t[i]
				i = (i + 1) // 2
			else:
				i //= 2
			if j % 2 == 0:
				s += self.t[j]
				j = (j - 1) // 2
			else:
				j //= 2
		return s + (self.t[i] if i == j else 0)