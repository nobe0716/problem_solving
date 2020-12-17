from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        prefix_sum = [[0] * (m) for _ in range(n)]

        prefix_sum[0][0] = mat[0][0]
        for i in range(1, n):
            prefix_sum[i][0] = prefix_sum[i - 1][0] + mat[i][0]

        for i in range(1, m):
            prefix_sum[0][i] = prefix_sum[0][i - 1] + mat[0][i]

        for i in range(1, n):
            for j in range(1, m):
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + mat[i][j]

        left = 0
        right = min(n, m)

        def is_possible(v):
            for i in range(v - 1, n):
                for j in range(v - 1, m):
                    c = prefix_sum[i][j]
                    if i - v >= 0:
                        c -= prefix_sum[i - v][j]
                    if j - v >= 0:
                        c -= prefix_sum[i][j - v]
                    if i - v >= 0 and j - v >= 0:
                        c += prefix_sum[i - v][j - v]
                    if c <= threshold:
                        return True
            return False

        res = 0
        while left <= right:
            v = (left + right) // 2
            if is_possible(v):
                res = v
                left = v + 1
            else:
                right = v - 1
        return res


s = Solution()

assert s.maxSideLength(mat=[[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], threshold=4) == 2
assert s.maxSideLength(mat=[[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]],
                       threshold=1) == 0
assert s.maxSideLength(mat=[[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], threshold=6) == 3
assert s.maxSideLength(mat=[[18, 70], [61, 1], [25, 85], [14, 40], [11, 96], [97, 96], [63, 45]], threshold=40184) == 2
