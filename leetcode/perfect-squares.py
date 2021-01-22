import sys
from functools import lru_cache

sys.setrecursionlimit(10001)

BASE = {i ** 2 for i in range(1, 100)}


class Solution:
    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        if n in BASE:
            return 1
        v = 1
        while v ** 2 <= n:
            v += 1
        v -= 1
        r = n
        for i in range(v, 0, -1):
            r = min(r, self.numSquares(n - i ** 2) + 1)
            if r == 2:
                return 2

        return r
