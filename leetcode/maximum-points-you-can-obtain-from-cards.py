from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        head_point = 0
        tail_point = sum(cardPoints[-k:])

        res = tail_point
        for i in range(k):
            head_point += cardPoints[i]
            tail_point -= cardPoints[-k + i]
            res = max(res, head_point + tail_point)

        return res
