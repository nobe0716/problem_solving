from collections import Counter
from collections import defaultdict
from typing import List


class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		nums = sorted(nums)
		n = len(nums)
		d = defaultdict(set)
		c = Counter(nums)
		for i in range(n - 1):
			for j in range(i + 1, n):
				two_sum = nums[i] + nums[j]
				d[two_sum].add((nums[i], nums[j]))



		r = set()
		if target % 2 == 0 and (target // 2) in d:
			combies = list(d[target // 2])
			for i in range(len(combies)):
				for j in range(i, len(combies)):
					r.add(tuple(sorted(combies[i] + combies[j])))

		key_set = set(d.keys())
		for key in sorted(key_set):
			if (target - key) not in key_set:
				continue
			combies_i = d[key]
			combies_j = d[target - key]

			for combie_i in combies_i:
				for combie_j in combies_j:
					r.add(tuple(sorted(combie_i + combie_j)))

		def possible(quadruplet):
			counter_quadruplet = Counter(quadruplet)
			for k, v in counter_quadruplet.items():
				if c[k] < v:
					return False
			return True

		return list(map(list, filter(possible, r)))


s = Solution()
print(s.fourSum([0, 4, -5, 2, -2, 4, 2, -1, 4], 12))
# print(s.fourSum([0, 1, 5, 0, 1, 5, 5, -4], 11))
# print(s.fourSum([0, 0, 0, 0], 1))
# print(s.fourSum([0, 0, 0, 0], 0))
# print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
