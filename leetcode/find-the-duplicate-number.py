class Solution(object):
	def findDuplicate(self, nums):
		n = len(nums) - 1
		m = (n + 1) / 2

		left = 1
		right = n
		while left < right:
			less = more = 0
			lb, rb = (right + left) // 2, (right + left + 1) // 2

			for i in nums:
				if left <= i <= lb:
					less += 1
				elif rb <= i <= right:
					more += 1

			if less > more:
				right = lb
			else:
				left = rb

		return left
