from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        r = s = 0
        for n in nums:
            s += n
            if s - k in d:
                r += d[s - k]
            d[s] += 1
        return r
