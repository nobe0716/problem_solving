from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r = float('-inf')
        max_t = [nums[0]]
        min_t = [nums[0]]
        for e in nums[1:]:
            a = max_t[-1] * e
            b = min_t[-1] * e
            max_t.append(max(e, a, b))
            min_t.append(min(e, a, b))

        return max(r, max(max_t), max(min_t))


s = Solution()
assert s.maxProduct([-4, -3, -2]) == 12
assert s.maxProduct([2, 3, -2, 4]) == 6
