from bisect import bisect
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        row = 0
        col = min(k - 1, m - 1)

        def calc_rank(v: int) -> int:
            return sum(bisect(_, v) for _ in matrix)

        res = matrix[n - 1][m - 1]
        while 0 <= row < n and 0 <= col < m:
            v = matrix[row][col]
            rank = calc_rank(v)
            if rank >= k:
                res = min(res, v)
                col -= 1
            else:
                row += 1
        return res


s = Solution()
assert s.kthSmallest([[1, 2], [3, 3]], 2) == 2
assert s.kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8, ) == 13
