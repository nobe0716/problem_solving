from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        num_of_blues = 0
        num_of_moments = 0
        status = [0] * len(light)
        for i, e in enumerate(light):
            status[e - 1] = 1
            while num_of_blues < len(light) and status[num_of_blues] == 1:
                num_of_blues += 1
            if num_of_blues == i + 1:
                num_of_moments += 1
        return num_of_moments


s = Solution()
assert s.numTimesAllBlue([4, 1, 2, 3]) == 1
assert s.numTimesAllBlue([2, 1, 3, 5, 4]) == 3
assert s.numTimesAllBlue([3, 2, 4, 1, 5]) == 2
assert s.numTimesAllBlue([2, 1, 4, 3, 6, 5]) == 3
