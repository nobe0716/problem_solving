import functools as functools
from typing import List


class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @functools.lru_cache(None)
        def solve(i, d):
            if l - i < d:
                return float('inf')
            if d == 1:
                return max(jobDifficulty[i:])

            r = float('inf')
            for j in range(i + 1, l):
                local_minimum = max(jobDifficulty[i:j]) + solve(j, d - 1)
                r = min(r, local_minimum)
            return r

        l = len(jobDifficulty)
        r = solve(0, d)
        return r if r != float('inf') else -1


s = Solution()

assert (s.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2) == 7)
assert (s.minDifficulty(jobDifficulty=[9, 9, 9], d=4) == -1)
assert (s.minDifficulty(jobDifficulty=[1, 1, 1], d=3) == 3)
assert (s.minDifficulty(jobDifficulty=[7, 1, 7, 1, 7, 1], d=3) == 15)
# print(s.minDifficulty(jobDifficulty=[11, 111, 22, 222, 33, 333, 44, 444], d=6))
assert (s.minDifficulty(jobDifficulty=[11, 111, 22, 222, 33, 333, 44, 444], d=6) == 843)
