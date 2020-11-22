import functools
import math
from itertools import combinations
from typing import List


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        @functools.lru_cache(None)
        def dist_square(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        res = float('inf')
        for pos in combinations(points, 4):
            a, b, c, d = map(tuple, sorted(pos))
            if a[1] > b[1] and c[1] > d[1]:
                c, d = d, c
            elif a[1] < b[1] and c[1] < d[1]:
                c, d = d, c
            ab = dist_square(a, b)
            cd = dist_square(c, d)
            if ab != cd:
                continue

            bc = dist_square(b, c)
            da = dist_square(d, a)
            if da != bc:
                continue

            ac = dist_square(a, c)
            bd = dist_square(b, d)
            if ac != bd:
                continue

            res = min(res, ab * bc)

        return math.sqrt(res) if res != float('inf') else 0.0


s = Solution()
assert s.minAreaFreeRect([[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]]) - 1.0 < 0.001
assert s.minAreaFreeRect([[1, 2], [2, 1], [1, 0], [0, 1]]) - 2.0 < 0.001
assert s.minAreaFreeRect([[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]]) - 0.0 < 0.001
