class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        r, c = 0, len(matrix[0]) - 1

        while c >= 0 and r < len(matrix):
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False