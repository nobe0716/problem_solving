from collections import deque
from typing import List

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def is_valid_coord(x: int, y: int):
            return 0 <= x < n and 0 <= y < m

        n, m = len(grid), len(grid[0])
        bfs_history = [[[float('inf') for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
        min_table = [[(float('inf'), float('inf')) for _ in range(m)] for _ in range(n)]

        q = deque([(0, 0, 0)])

        bfs_history[0][0][0] = 0
        min_table[0][0] = (0, 0)
        while q:
            x, y, w = q.popleft()
            c = bfs_history[x][y][w]
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if not is_valid_coord(nx, ny):
                    continue
                nw = w + grid[nx][ny]
                if nw > k or c + 1 >= bfs_history[nx][ny][nw]:
                    continue
                if c >= min_table[nx][ny][0] and nw >= min_table[nx][ny][1]:
                    continue
                bfs_history[nx][ny][nw] = c + 1
                if min_table[nx][ny][0] > c + 1:
                    min_table[nx][ny] = (c + 1, nw)
                q.append((nx, ny, nw))

        return min_table[n - 1][m - 1][0] if min_table[n - 1][m - 1][0] != float('inf') else -1


s = Solution()
assert s.shortestPath([[0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0]], 1) == 13

assert s.shortestPath(grid=[[0] * 40 for _ in range(40)], k=1600) == 78
assert s.shortestPath(grid=
                      [[0, 0, 0],
                       [1, 1, 0],
                       [0, 0, 0],
                       [0, 1, 1],
                       [0, 0, 0]],
                      k=1) == 6
assert s.shortestPath(grid=
                      [[0, 1, 1],
                       [1, 1, 1],
                       [1, 0, 0]],
                      k=1) == -1
#
