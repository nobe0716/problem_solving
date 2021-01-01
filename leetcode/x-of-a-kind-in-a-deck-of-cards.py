import math
from collections import Counter
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        cards = list(reversed(c.most_common()))
        if cards[0][1] < 2:
            return False
        gcd = cards[0][1]
        for e in cards:
            gcd = math.gcd(gcd, e[1])
        return gcd > 1


s = Solution()
assert not s.hasGroupsSizeX(deck=[1])
assert s.hasGroupsSizeX(deck=[1, 2, 3, 4, 4, 3, 2, 1])
