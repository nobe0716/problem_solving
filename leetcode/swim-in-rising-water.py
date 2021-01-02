import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        depth = grid[0][0]
        n, m = len(grid), len(grid[0])
        visited = {(0, 0)}
        h = [(depth, 0, 0)]
        while h and (n - 1, m - 1) not in visited:
            d, x, y = heapq.heappop(h)
            depth = max(d, depth)
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if not (0 <= nx < n) or not (0 <= ny < m) or (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                heapq.heappush(h, (grid[nx][ny], nx, ny))

        return max(depth, grid[n - 1][m - 1])


s = Solution()
assert s.swimInWater([[0, 2], [1, 3]]) == 3
assert s.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]) == 16
