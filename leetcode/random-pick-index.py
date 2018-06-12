import random
class Solution(object):

	def __init__(self, nums):
		self.nums = nums


	def pick(self, target):
		target_count = 0
		pos = None
		for i, n in enumerate(self.nums):
			if n == target:
				if random.randint(0, target_count) == 0:
					pos = i
				target_count += 1
		return pos