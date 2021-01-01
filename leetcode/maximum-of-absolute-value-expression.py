from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        res = float('-inf')
        elems = [list() for _ in range(4)]

        # [[a + b + i, a - b + i, a + b - i, a - b - i] for i, a, b in zip(range(n), arr1, arr2)]
        for i, a, b in zip(range(n), arr1, arr2):
            elems[0].append(a + b + i)
            elems[1].append(a - b + i)
            elems[2].append(a + b - i)
            elems[3].append(a - b - i)
        for _ in elems:
            res = max(res, max(_) - min(_))
        return res


s = Solution()
assert s.maxAbsValExpr([-9, 0, -5, -7, 10, 6, 1, -8, -4], [7, 0, -5, 4, 7, 8, 1, -7, 6]) == 35
assert s.maxAbsValExpr(arr1=[1, -2, -5, 0, 10], arr2=[0, -2, -1, -7, -4]) == 20
assert s.maxAbsValExpr(arr1=[1, 2, 3, 4], arr2=[-1, 4, 5, 6]) == 13
