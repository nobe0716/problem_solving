from typing import List

dx = [None, 0, 0, 1, -1]
dy = [None, 1, -1, 0, 0]


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        group_info = [[0] * m for _ in range(n)]

        def is_valid_coord(x: int, y: int):
            return 0 <= x < n and 0 <= y < m

        def expand_group(x: int, y: int, group: int):
            stack = [(x, y)]
            visited = set()
            while stack:
                x, y = stack.pop()
                if not is_valid_coord(x, y) or group_info[x][y] > 0:
                    continue
                visited.add((x, y))
                group_info[x][y] = group
                d = grid[x][y]
                stack.append((x + dx[d], y + dy[d]))
            return visited

        group_count = 1
        q = expand_group(0, 0, 1)
        while q and group_info[n - 1][m - 1] == 0:
            nq = set()
            for x, y in q:
                for i in range(1, 5):
                    nx, ny = x + dx[i], y + dy[i]
                    if not is_valid_coord(nx, ny) or group_info[nx][ny] > 0:
                        continue
                    nq |= expand_group(nx, ny, group_count + 1)
            q = nq
            group_count += 1
        return group_info[n - 1][m - 1] - 1


s = Solution()
assert s.minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]) == 3
assert s.minCost(grid=[[1, 1, 3], [3, 2, 2], [1, 1, 4]]) == 0
assert s.minCost(grid=[[1, 2], [4, 3]]) == 1
assert s.minCost(grid=[[2, 2, 2], [2, 2, 2]]) == 3
assert s.minCost(grid=[[4]]) == 0
