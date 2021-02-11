from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        r = []
        for e in asteroids:
            if e > 0:
                stack.append(e)
            elif e < 0:
                while stack and stack[-1] < -e:
                    stack.pop()

                if not stack:
                    r.append(e)
                elif stack[-1] == -e:
                    stack.pop()

        r += stack
        return r


s = Solution()
assert s.asteroidCollision([10, 2, -5]) == [10]
assert s.asteroidCollision([5, 10, -5]) == [5, 10]
assert s.asteroidCollision([8, -8]) == []
assert s.asteroidCollision([10, 2, -5]) == [10]
assert s.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
