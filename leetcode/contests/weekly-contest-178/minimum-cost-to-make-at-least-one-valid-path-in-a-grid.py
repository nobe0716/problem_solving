import sys
from typing import List

sys.setrecursionlimit(1_000_000)
di = [0, 0, 0, 1, -1]
dj = [0, 1, -1, 0, 0]

MAX_VAL = 1_000_000
IS_DEBUG = False


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def is_valid_coord(x, y):
            return (0 <= x < m and 0 <= y < n)

        def print_table():
            if not IS_DEBUG:
                return
            for i in range(m):
                for j in range(n):
                    if table[i][j] == MAX_VAL:
                        print('?', end=' ')
                    else:
                        print(table[i][j], end=' ')
                print('')

        def fill_table(i, j, v):
            if not is_valid_coord(i, j) or table[i][j] != MAX_VAL:
                return []
            table[i][j] = v
            k = grid[i][j]
            return [(i, j)] + fill_table(i + di[k], j + dj[k], v)

        m, n = len(grid), len(grid[0])
        table = [[MAX_VAL] * n for _ in range(m)]
        # table[1][1] = 0
        v = 0
        pos_queue = fill_table(0, 0, v)

        while pos_queue and table[m - 1][n - 1] == MAX_VAL:
            print_table()
            new_pos = []
            v += 1
            for i, j in pos_queue:
                for k in range(1, 5):
                    x, y = i + di[k], j + dj[k]
                    if is_valid_coord(x, y) and table[x][y] == MAX_VAL:
                        new_pos.append((x, y))

            pos_queue = set()
            for i, j in new_pos:
                for x, y in fill_table(i, j, v):
                    pos_queue.add((x, y))

        print_table()

        return v


if __name__ == '__main__':
    s = Solution()
    IS_DEBUG = True
    assert s.minCost(grid=[[1, 2], [4, 3]]) == 1
    assert s.minCost(grid=[[2, 2, 2], [2, 2, 2]]) == 3
    assert s.minCost(grid=[[4]]) == 0
    assert s.minCost(grid=[[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]) == 3
    assert s.minCost(grid=[[1, 1, 3], [3, 2, 2], [1, 1, 4]]) == 0
