from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        while any(x != 1 for x in target):
            target = sorted(target)
            target[-1] -= (sum(target) - target[-1])
            if target[-1] < 1:
                return False
        return True


s = Solution()
print(s.isPossible([9, 9, 9]))
print(s.isPossible([9, 3, 5]))
print(s.isPossible([1, 1, 1, 2]))
print(s.isPossible([8, 5]))
