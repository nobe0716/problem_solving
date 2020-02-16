class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        s = prices[0]
        m = 0
        for e in prices[1:]:
            m = max(m, e - s)
            s = min(s, e)
        return m
