import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        prefix_sum = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                prefix_sum[i][j] = matrix[i][j]
                if i > 0 and j > 0:
                    prefix_sum[i][j] -= prefix_sum[i - 1][j - 1]
                if i > 0:
                    prefix_sum[i][j] += prefix_sum[i - 1][j]
                if j > 0:
                    prefix_sum[i][j] += prefix_sum[i][j - 1]

        res = float('-inf')
        for i1 in range(n):
            for i2 in range(i1, n):
                base = [prefix_sum[i2][j] - (prefix_sum[i1 - 1][j] if i1 > 0 else 0) for j in range(m)]

                values = []
                for e in base:
                    if e <= k:
                        res = max(res, e)
                    idx = bisect.bisect_left(values, e - k)
                    if idx < len(values) and e - values[idx] <= k:
                        res = max(res, e - values[idx])
                    bisect.insort_right(values, e)
        return res


s = Solution()
assert s.maxSumSubmatrix(matrix=[[2, 2, -1]], k=3) == 3
assert s.maxSumSubmatrix([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 10) == 10
assert s.maxSumSubmatrix([[2, 2, -1]], 0) == -1
assert s.maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2) == 2
