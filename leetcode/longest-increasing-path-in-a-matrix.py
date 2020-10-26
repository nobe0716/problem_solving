import functools
import sys
from typing import List

sys.setrecursionlimit(1_000_000)


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def is_valid_pos(x: int, y: int) -> bool:
            return 0 <= x < n and 0 <= y < m

        def np(x: int, y: int):
            yield x - 1, y
            yield x, y + 1
            yield x + 1, y
            yield x, y - 1

        @functools.lru_cache(None)
        def dp(x: int, y: int) -> int:
            candidates = [0]
            for nx, ny in np(x, y):
                if not is_valid_pos(nx, ny):
                    continue
                if matrix[x][y] >= matrix[nx][ny]:
                    continue
                candidates.append(dp(nx, ny))
            return max(candidates) + 1

        if not matrix:
            return 0

        n, m = len(matrix), len(matrix[0])

        res = 0
        for x in range(n):
            for y in range(m):
                res = max(res, dp(x, y))

        return res


s = Solution()
assert s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
assert s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
assert s.longestIncreasingPath([[19, 10, 19, 10, 19, 10, 3, 1, 6, 12, 10, 0, 4, 4, 3, 4, 17, 2, 3, 15, 6, 6, 8, 18],
                                [1, 17, 0, 2, 0, 12, 2, 16, 9, 4, 8, 6, 9, 13, 6, 12, 11, 13, 2, 1, 12, 16, 10, 4],
                                [18, 17, 6, 6, 2, 0, 19, 0, 19, 12, 17, 18, 13, 1, 19, 11, 10, 6, 3, 13, 8, 1, 12, 6],
                                [8, 3, 1, 5, 3, 15, 13, 6, 4, 7, 16, 9, 9, 10, 6, 2, 0, 15, 10, 19, 18, 6, 3, 11],
                                [10, 5, 6, 10, 17, 14, 3, 18, 5, 19, 18, 4, 0, 4, 18, 5, 7, 12, 14, 17, 8, 19, 12, 13],
                                [18, 13, 11, 1, 12, 16, 9, 1, 5, 17, 15, 17, 11, 8, 17, 0, 17, 5, 17, 6, 15, 7, 10, 3],
                                [2, 0, 7, 0, 6, 8, 19, 17, 18, 11, 17, 0, 2, 10, 13, 4, 10, 18, 12, 18, 14, 16, 6, 6],
                                [14, 8, 18, 0, 5, 13, 0, 12, 3, 7, 18, 12, 16, 12, 4, 13, 15, 5, 19, 8, 16, 12, 13, 9],
                                [19, 0, 3, 5, 3, 9, 11, 2, 14, 10, 13, 0, 1, 17, 10, 10, 4, 12, 9, 19, 13, 11, 3, 9],
                                [15, 7, 9, 2, 7, 11, 15, 19, 18, 18, 3, 2, 17, 3, 16, 12, 6, 17, 15, 3, 16, 15, 1, 2],
                                [3, 5, 11, 11, 5, 13, 15, 6, 5, 16, 19, 12, 15, 9, 16, 3, 0, 17, 8, 9, 12, 14, 13, 1],
                                [10, 2, 10, 9, 13, 7, 13, 18, 10, 8, 5, 2, 9, 19, 16, 16, 0, 6, 1, 7, 2, 5, 19,
                                 0]]) == 8
