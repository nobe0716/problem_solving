from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def remove_island(x: int, y: int):
            if not (0 <= x < n and 0 <= y < m) or grid[x][y] != '1':
                return
            grid[x][y] = 0
            remove_island(x + 1, y)
            remove_island(x - 1, y)
            remove_island(x, y + 1)
            remove_island(x, y - 1)

        n, m = len(grid), len(grid[0])
        c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    remove_island(i, j)
                    c += 1
        return c
