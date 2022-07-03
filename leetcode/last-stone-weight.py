import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        while len(stones) >= 2:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            r = -abs((-a) - (-b))
            heapq.heappush(stones, r)
        return stones[0]

