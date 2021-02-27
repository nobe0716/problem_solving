from collections import Counter
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def calc(s: str) -> int:
            if not s or s == '':
                return 0
            c = Counter(s)
            return c[sorted(c.keys())[0]]

        wc = Counter([calc(s) for s in words])
        wc = [wc[i] for i in range(2001)]

        res = []
        for query in queries:
            v = calc(query)
            res.append(sum(wc[v + 1:]))

        return res


s = Solution()
assert s.numSmallerByFrequency(queries=["cbd"], words=["zaaaz"]) == [1]
assert s.numSmallerByFrequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]) == [1, 2]
