class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for row in grid:
            c += len(list(filter(lambda x: x < 0, row)))
        return c
