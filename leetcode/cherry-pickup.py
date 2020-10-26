import functools
import sys
from typing import List

sys.setrecursionlimit(50 ** 4)


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def pre_pos(x: int, y: int):
            if x and grid[x - 1][y] >= 0:
                yield x - 1, y
            if y and grid[x][y - 1] >= 0:
                yield x, y - 1

        @functools.lru_cache(None)
        def dp(i: int, j: int, k: int, l: int):
            if i == j == k == l == 0:
                return grid[0][0]
            if grid[i][j] == -1 or grid[k][l] == -1:
                return -1

            candidates = []
            for pi, pj in pre_pos(i, j):
                for pk, pl in pre_pos(k, l):
                    sub_sol = dp(pi, pj, pk, pl)
                    if sub_sol >= 0:
                        candidates.append(sub_sol)
            if not candidates:
                return -1
            bonus = grid[i][j] + (grid[k][l] if i != k or j != l else 0)
            return bonus + max(candidates)

        n = len(grid)
        r = dp(n - 1, n - 1, n - 1, n - 1)
        return max(r, 0)


# [[1,1,-1],
#  [1,-1,1],
#  [-1,1,1]]
s = Solution()
assert s.cherryPickup([[1, 1, -1], [1, -1, 1], [-1, 1, 1]]) == 0
assert s.cherryPickup([[0, 1, -1], [1, 0, -1], [1, 1, 1]]) == 5
