from functools import lru_cache


class Solution:
    @lru_cache(None)
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        return min(self.integerReplacement(n - 1), self.integerReplacement(n + 1)) + 1


s = Solution()
assert s.integerReplacement(2 ** 15 - 1)
