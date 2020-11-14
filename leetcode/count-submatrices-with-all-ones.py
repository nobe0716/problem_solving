from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0

        n, m = len(mat), len(mat[0])

        cols = [[0] * m for _ in range(n)]

        for j in range(m):
            cols[0][j] = 1 if mat[0][j] else 0
            for i in range(1, n):
                cols[i][j] = cols[i - 1][j] + 1 if mat[i][j] else 0

        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    continue
                min_height = float('inf')
                for k in range(j, -1, -1):
                    if mat[i][k] == 0:
                        break
                    min_height = min(min_height, cols[i][k])
                    res += min_height
        return res


s = Solution()
assert s.numSubmat([
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 1, 0]]) == 24
