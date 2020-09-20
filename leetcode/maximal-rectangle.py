from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])

        """
        t[i][j] represent (rows, cols) of largest rectangle, which contains matrix[i][j] 
        """
        heights = [0] * cols

        res = 0
        for i in range(rows):
            stack = []
            for j in range(cols):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
                    # width = 1

                left_pos = j
                while stack and stack[-1][0] >= heights[j]:
                    left_height, left_idx = stack.pop()
                    left_width = j - left_idx
                    res = max(res, left_height * left_width)
                    left_pos = left_idx
                if heights[j] > 0:
                    stack.append((heights[j], left_pos))
            while stack:
                left_height, left_idx = stack.pop()
                left_width = cols - left_idx
                res = max(res, left_height * left_width)

        return res

# s = Solution()
# assert s.maximalRectangle(
#     [["1", "0", "1", "1", "0", "1"],
#      ["1", "1", "1", "1", "1", "1"],
#      ["0", "1", "1", "0", "1", "1"],
#      ["1", "1", "1", "0", "1", "0"],
#      ["0", "1", "1", "1", "1", "1"],
#      ["1", "1", "0", "1", "1", "1"]]) == 8
#
# assert s.maximalRectangle(
#     [["0", "0", "0", "1", "0", "1", "0"],
#      ["0", "1", "0", "0", "0", "0", "0"],
#      ["0", "1", "0", "1", "0", "0", "1"],
#      ["0", "0", "1", "1", "0", "0", "1"],
#      ["1", "1", "1", "1", "1", "1", "0"],
#      ["1", "0", "0", "1", "0", "1", "1"],
#      ["0", "1", "0", "0", "1", "0", "1"],
#      ["1", "1", "0", "1", "1", "1", "0"],
#      ["1", "0", "1", "0", "1", "0", "1"],
#      ["1", "1", "1", "0", "0", "0", "0"]]) == 6
#
# assert s.maximalRectangle([["1", "1"]]) == 2
# assert s.maximalRectangle([["0", "1"]]) == 1
# assert s.maximalRectangle([["0", "1"], ["0", "1"]]) == 2
# assert s.maximalRectangle(
#     [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]) == 6
