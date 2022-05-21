from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        c = len(colSum)
        r = len(rowSum)
        table = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                table[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= table[i][j]
                colSum[j] -= table[i][j]
        return table

