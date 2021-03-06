from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def calc_area(x: int, y: int):
            if grid[x][y] != 1:
                return 0
            grid[x][y] = 2
            c = 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] != 1:
                    continue
                c += calc_area(nx, ny)
            return c

        n, m = len(grid), len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                res = max(res, calc_area(i, j))
        return res
