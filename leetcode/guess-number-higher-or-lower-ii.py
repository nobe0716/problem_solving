import functools


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @functools.lru_cache(None)
        def dp(lo: int, hi: int) -> int:
            if lo == hi:
                return 0
            if lo + 1 == hi:
                return lo
            elif lo > hi:
                return 0
            return min(i + max(dp(lo, i - 1), dp(i + 1, hi)) for i in range(lo, hi))

        return dp(1, n)


s = Solution()
assert (s.getMoneyAmount(1) == 0)
assert (s.getMoneyAmount(2) == 1)
assert (s.getMoneyAmount(3) == 2)
assert (s.getMoneyAmount(4) == 4)
assert (s.getMoneyAmount(7) == 10)
assert (s.getMoneyAmount(10) == 16)
