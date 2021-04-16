from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    continue

                def dfs(x: int, y: int) -> bool:
                    if x < 0 or x >= n or y < 0 or y >= m:
                        return False
                    if grid[x][y] > 0:
                        return True
                    grid[x][y] = 2
                    is_closed = True
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if not dfs(nx, ny):
                            is_closed = False
                    return is_closed

                if dfs(i, j):
                    res += 1

        return res


s = Solution()
assert s.closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]) == 2
assert s.closedIsland(grid=[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]) == 1
assert s.closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 0, 0, 1],
                            [1, 0, 1, 1, 1, 0, 1],
                            [1, 0, 1, 0, 1, 0, 1],
                            [1, 0, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 1]]) == 2
