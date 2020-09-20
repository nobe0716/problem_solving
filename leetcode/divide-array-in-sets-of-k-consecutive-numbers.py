from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        for basis in sorted(c.keys()):
            if not c[basis]:
                continue

            w = c[basis]
            for i in range(basis, basis + k):
                if c[i] < w:
                    return False
                c[i] -= w

        return True


s = Solution()
assert s.isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 4)
