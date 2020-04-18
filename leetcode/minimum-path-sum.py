import functools


class Solution:
    def minPathSum(self, grid):
        @functools.lru_cache(None)
        def get_min_path_sum(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            elif i == 0:
                return grid[i][j] + get_min_path_sum(i, j - 1)
            elif j == 0:
                return grid[i][j] + get_min_path_sum(i - 1, j)
            return grid[i][j] + min(get_min_path_sum(i - 1, j), get_min_path_sum(i, j - 1))

        return get_min_path_sum(len(grid) - 1, len(grid[0]) - 1)
