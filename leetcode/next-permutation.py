class Solution(object):
	def nextPermutation(self, nums):
		l = len(nums)
		if l <= 1:
			return
		idx = l - 2
		while nums[idx] >= nums[idx + 1] and idx >= 0:
			idx -= 1

		if idx == -1:
			nums[0:] = list(reversed(nums))
			return
		i = l - 1
		while i > idx:
			if nums[idx] < nums[i]:
				nums[idx], nums[i] = nums[i], nums[idx]
				break
			i -= 1
		nums[idx + 1:l] = list(reversed(nums[idx + 1:l]))