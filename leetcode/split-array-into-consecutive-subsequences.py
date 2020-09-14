from collections import defaultdict
import heapq
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap_dict = defaultdict(list)
        for e in nums:
            if not heap_dict[e - 1]:
                heapq.heappush(heap_dict[e], 1)
            else:
                min_len = heapq.heappop(heap_dict[e - 1])
                heapq.heappush(heap_dict[e], min_len + 1)
        return all(not h or heapq.heappop(h) >= 3 for h in heap_dict.values())


s = Solution()
assert s.isPossible([1, 2, 3, 3, 4, 5])
assert s.isPossible([1, 2, 3, 3, 4, 4, 5, 5])
assert not s.isPossible([1, 2, 3, 4, 4, 5])
assert s.isPossible([1,2,3,3,4,4,5,5])
