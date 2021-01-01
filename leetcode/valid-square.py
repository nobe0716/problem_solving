from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def get_dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        p = sorted([p1, p2, p3, p4])
        return get_dist(p[0], p[1]) > 0 and get_dist(p[0], p[1]) == get_dist(p[0], p[2]) == get_dist(p[2], p[3]) == get_dist(p[1], p[3]) and get_dist(p[0], p[3]) == get_dist(p[1], p[2])
