import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for e in stones:
            heapq.heappush(h, -e)

        while len(h) >= 2:
            a, b = -heapq.heappop(h), -heapq.heappop(h)
            heapq.heappush(h, -(a - b))
        return -h[0]
