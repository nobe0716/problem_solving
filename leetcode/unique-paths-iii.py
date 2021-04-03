from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        route_count = 1

        start_pos = None
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    route_count += 1
                elif grid[i][j] == 1:
                    start_pos = i, j
                elif grid[i][j] == 2:
                    end_pos = i, j

        route = set()
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

        def back(x: int, y: int) -> int:
            if len(route) == route_count - 1:
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) and grid[nx][ny] == 2:
                        # print(route)
                        return 1
                return 0
            res = 0
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in route and grid[nx][ny] == 0:
                    route.add((nx, ny))
                    res += back(nx, ny)
                    route.remove((nx, ny))
            return res

        ans = back(*start_pos)
        # print('ans: {}'.format(ans))
        return ans


s = Solution()
assert s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2
assert s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4
assert s.uniquePathsIII([[0, 1], [2, 0]]) == 0
