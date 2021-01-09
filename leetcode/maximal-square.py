from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        col = [[0] * m for _ in range(n)]
        for i in range(m):
            col[0][i] = 1 if matrix[0][i] == "1" else 0
        for i in range(1, n):
            for j in range(m):
                col[i][j] = col[i - 1][j] + 1 if matrix[i][j] == "1" else 0

        res = 0
        for i in range(n):
            for j in range(res, m):
                for k in range(res + 1, min(i, j) + 2):  # k - possible answer candidate
                    if all(matrix[i][_] == "1" and col[i][_] >= k for _ in range(j - k + 1, j + 1)):
                        res = k
                        break
        return res ** 2


s = Solution()
assert s.maximalSquare(matrix=[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]) == 4
assert s.maximalSquare(matrix=[["1", "1", "1", "0", "0"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]) == 9
assert s.maximalSquare(matrix=[["0", "1"], ["1", "0"]]) == 1
assert s.maximalSquare(matrix=[["0"]]) == 0
