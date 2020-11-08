import functools


class Solution:
    def minInsertions(self, s: str) -> int:
        @functools.lru_cache(None)
        def dp(lo=0, hi=len(s)):
            if hi - lo <= 1:
                return 0
            if s[lo] == s[hi - 1]:
                return dp(lo + 1, hi - 1)
            return 1 + min(dp(lo + 1, hi), dp(lo, hi - 1))

        return dp()
