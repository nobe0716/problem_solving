from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # t = [i_pos_of_both_robot1][j_pos_of_robot1][j_pos_of_robot2]
        t = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        t[0][0][m - 1] = grid[0][0] + grid[0][m - 1]

        for i in range(1, n):
            for j in range(min(m, i + 1)):  # j; pos of robot 1
                for k in range(max(m - i - 1, 0), m):  # k; pos of robot2
                    for pj in range(max(j - 1, 0), min(m, j + 2)):
                        for pk in range(max(k - 1, 0), min(m, k + 2)):
                            t[i][j][k] = max(t[i][j][k],
                                             t[i - 1][pj][pk] + (grid[i][j] + grid[i][k] if j != k else grid[i][j]))
        return max(t[n - 1][j][k] for j in range(m) for k in range(m))


s = Solution()
assert s.cherryPickup([[0, 8, 7, 10, 9, 10, 0, 9, 6], [8, 7, 10, 8, 7, 4, 9, 6, 10], [8, 1, 1, 5, 1, 5, 5, 1, 2],
                       [9, 4, 10, 8, 8, 1, 9, 5, 0], [4, 3, 6, 10, 9, 2, 4, 8, 10], [7, 3, 2, 8, 3, 3, 5, 9, 8],
                       [1, 2, 6, 5, 6, 2, 0, 10, 0]]) == 96
assert s.cherryPickup(grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]) == 24
assert s.cherryPickup(grid=[[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                            [1, 0, 2, 3, 0, 0, 6]]) == 28
assert s.cherryPickup(grid=[[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]) == 22
assert s.cherryPickup(grid=[[1, 1], [1, 1]]) == 4
