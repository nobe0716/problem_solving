from typing import List


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        a, b = 1, 1
        return a * x + b * y


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        res = []
        for x in range(1, 1000):
            lo, hi = 1, 1000

            while lo <= hi:
                y = (lo + hi) // 2
                v = customfunction.f(x, y)

                if v == z:
                    res.append([x, y])
                    break
                elif v > z:
                    hi = y - 1
                else:
                    lo = y + 1

        return res


s = Solution()
assert s.findSolution(CustomFunction, 10) == [[1, 4], [2, 3], [3, 2], [4, 1]]
