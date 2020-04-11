from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                r += prices[i + 1] - prices[i]
        return r
