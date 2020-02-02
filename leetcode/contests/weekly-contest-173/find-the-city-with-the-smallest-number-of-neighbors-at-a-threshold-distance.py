from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        t = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            t[i][i] = 0
        for from_i, to_i, weight_i in edges:
            t[from_i][to_i] = t[to_i][from_i] = weight_i
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    t[i][j] = min(t[i][j], t[i][k] + t[k][j])

        # for i in range(n):
        #     for j in range(n):
        #         print('{}'.format(t[i][j]), end=' ')
        #     print()

        min_i, min_s = None, float('inf')
        for i in range(n):
            s = len(list(filter(lambda x: x <= distanceThreshold, t[i])))
            if min_s >= s:
                min_s = s
                min_i = i

            # print(i, s)
        return min_i


s = Solution()
assert s.findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4) == 3
print(s.findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], distanceThreshold=2))
