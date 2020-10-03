import bisect
import random
from collections import Counter
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.a = [w[0]]
        for e in w[1:]:
            self.a.append(self.a[-1] + e)

    def pickIndex(self) -> int:
        v = random.randint(0, self.a[-1] - 1)
        if v < self.a[0]:
            return 0
        idx = bisect.bisect(self.a, v)
        return idx


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 3])
print(sorted(Counter(obj.pickIndex() for _ in range(4)).items()))
