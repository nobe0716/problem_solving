# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def get(self, x: int, y: int) -> int:
        return None

    def dimensions(self) -> list[int]:
        return None


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        lmc = float('inf')

        for i in range(n):
            l, r = 0, m - 1
            v = float('inf')
            while l < r:
                p = (l + r) // 2
                if binaryMatrix.get(i, p) == 0:
                    l = p + 1
                else:
                    r = p - 1
                    v = p

            lmc = min(v, lmc)
        return -1 if lmc == float('inf') else lmc
