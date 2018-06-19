class Solution(object):
	def maxArea(self, height):
		l, r = 0, len(height) - 1
		v = 0
		while l < r:
			lh, rh = height[l], height[r]
			v = max(v, (r - l) * min(lh, rh))
			if lh > rh:
				r -= 1
			else:
				l += 1
		return v