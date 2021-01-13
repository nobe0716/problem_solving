from collections import defaultdict
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_to_y = defaultdict(set)
        y_to_x = defaultdict(set)

        for x, y in points:
            x_to_y[x].add(y)
            y_to_x[y].add(x)

        sorted_x = sorted(x_to_y.keys())
        len_x = len(sorted_x)
        res = float('inf')

        for i in range(len_x - 1):
            x1 = sorted_x[i]
            y_set_1 = x_to_y[x1]
            if len(y_set_1) < 2:
                continue

            for j in range(i + 1, len_x):
                x2 = sorted_x[j]
                y_set_2 = x_to_y[x2]
                if len(y_set_2) < 2:
                    continue

                candidates = y_set_1 & y_set_2
                if len(candidates) < 2:
                    continue

                candidates = sorted(candidates)
                res = min(res, (x2 - x1) * min(candidates[k + 1] - candidates[k] for k in range(len(candidates) - 1)))
        return res if res != float('inf') else 0


s = Solution()
assert s.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]) == 4
assert s.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]) == 2
