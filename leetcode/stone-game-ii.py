import sys
from functools import lru_cache
from typing import List

sys.setrecursionlimit(1000)


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def alex(i: int, m: int) -> int:
            if i >= n:
                return 0
            elif i + m >= n:
                return acc_sum[i]
            return max(acc_sum[i] - lee(i + j, max(j, m)) for j in range(1, 2 * m + 1))

        @lru_cache(None)
        def lee(i: int, m: int) -> int:
            if i >= n:
                return 0
            elif i + m >= n:
                return acc_sum[i]
            return max(acc_sum[i] - alex(i + j, max(j, m)) for j in range(1, 2 * m + 1))

        n = len(piles)
        acc_sum = [0] * (n - 1) + [piles[-1]]
        for i in range(n - 2, -1, -1):
            acc_sum[i] = acc_sum[i + 1] + piles[i]

        res = alex(0, 1)
        return res


s = Solution()
assert s.stoneGameII(piles=[1, 2, 3, 4, 5, 100]) == 104
assert s.stoneGameII(piles=[2, 7, 9, 4, 4]) == 10
# assert s.stoneGameII(piles=[1] * 100) == 10
