import functools
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        @functools.lru_cache(None)
        def dp(s: str) -> int:
            v = [1]
            for i in range(len(s)):
                t = s[0:i] + s[i + 1:]
                if t in word_set:
                    v.append(dp(t) + 1)
            return max(v)

        word_set = set(words)
        return max(map(dp, words))


s = Solution()
assert s.longestStrChain(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5
assert s.longestStrChain(words=["a", "b", "ba", "bca", "bda", "bdca"]) == 4
