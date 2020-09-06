from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        c = Counter(hand)
        keys = sorted(c.keys())

        for key in keys:
            if c[key] <= 0:
                continue
            count = c[key]
            for i in range(W):
                if c[key + i] < count:
                    return False
                c[key + i] -= count

        return True


s = Solution()
assert s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
assert s.isNStraightHand([1, 2, 3, 4, 5], 4) == False
assert s.isNStraightHand([7, 6, 9, 7, 884543359, 387569973, 6, 8, 9, 8], 4)
print('fin')
