from collections import Counter
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = Counter()
        res = 0
        target = [i * 60 for i in range(1, 1000 // 60 + 1)]
        for e in time:
            for t in target:
                if (t - e) not in c:
                    continue
                res += c[t - e]
            c[e] += 1
        return res
