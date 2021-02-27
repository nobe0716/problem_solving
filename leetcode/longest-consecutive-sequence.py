from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # num_to_pos = {n: i for i, n in enumerate(nums)}
        res = 0
        ns = set(nums)
        for e in nums:
            if (e - 1) in ns:
                continue
            n = e
            while n in ns:
                n = n + 1
            res = max(n - e, res)

        return res


s = Solution()
assert s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4
assert s.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
