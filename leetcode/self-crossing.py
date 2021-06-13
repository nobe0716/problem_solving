from typing import List


class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        a = b = c = d = e = f = 0
        for a in x:
            if d >= b > 0 and (c <= a or 0 <= c - e <= a and b + f >= d):
                return True
            b, c, d, e, f = a, b, c, d, e
        return False


s = Solution()
assert not s.isSelfCrossing([3, 3, 3, 2, 1, 1])
assert not s.isSelfCrossing([1, 2, 3, 4])
assert s.isSelfCrossing([1, 1, 2, 1, 1])
