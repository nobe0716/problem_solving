from collections import Counter
from operator import itemgetter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        e = c.most_common()[:k]
        return list(map(itemgetter(0), e))


s = Solution()
assert s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]
