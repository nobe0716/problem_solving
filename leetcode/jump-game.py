class Solution:
	def canJump(self, nums):
		l = len(nums)
		maximum_rechable_idx = 0
		for i, n in enumerate(nums):
			if i > maximum_rechable_idx:
				break
			maximum_rechable_idx = max(maximum_rechable_idx, i + n)
		return maximum_rechable_idx >= l - 1