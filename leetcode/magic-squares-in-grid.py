from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(x: int, y: int) -> bool:
            col_sum, row_sum, dia_sum = [0, 0, 0], [0, 0, 0], [0, 0]
            ws = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    v = grid[i][j]
                    col_sum[j - y] += v
                    row_sum[i - x] += v
                    if i - x == j - y:
                        dia_sum[0] += v
                    if (i - x) + (j - y) == 2:
                        dia_sum[1] += v

                    ws.add(v)
                    if len(ws) > 1:
                        return False
            return len(set(col_sum) | set(row_sum) | set(dia_sum)) == 1

        n, m = len(grid), len(grid[0])
        c = 0
        for i in range(n - 2):
            for j in range(m - 2):
                if is_magic(i, j):
                    c += 1
        return c


s = Solution()

assert s.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]) == 1
