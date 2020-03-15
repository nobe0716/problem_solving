from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        luckies = []
        n = range(len(matrix))
        for i in n:
            for j in range(len(matrix[i])):
                if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max(matrix[k][j] for k in n):
                    luckies.append(matrix[i][j])
        # print(luckies)
        return luckies


s = Solution()
assert s.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]) == [15]
