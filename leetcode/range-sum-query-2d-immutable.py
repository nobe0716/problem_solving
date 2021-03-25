from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.acc_sum = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    self.acc_sum[i][j] = matrix[i][j]
                elif i == 0:
                    self.acc_sum[i][j] = matrix[i][j] + self.acc_sum[i][j - 1]
                elif j == 0:
                    self.acc_sum[i][j] = matrix[i][j] + self.acc_sum[i - 1][j]
                else:
                    self.acc_sum[i][j] = matrix[i][j] + self.acc_sum[i - 1][j] + self.acc_sum[i][j - 1] - self.acc_sum[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        v = self.acc_sum[row2][col2]
        if row1 > 0:
            v -= self.acc_sum[row1 - 1][col2]
        if col1 > 0:
            v -= self.acc_sum[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            v += self.acc_sum[row1 - 1][col1 - 1]
        return v
