import math
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.count = len(nums)
        self.offset = 2 ** int(math.ceil(math.log2(self.count)))
        self.table = [0] * (self.offset * 2 + 1)
        for i in range(self.count):
            self.table[self.offset + i] = nums[i]
        for i in range(self.offset - 1, 0, -1):
            self.table[i] = self.table[i * 2] + self.table[i * 2 + 1]

    def update(self, index: int, val: int) -> None:
        i = self.offset + index
        diff = val - self.table[i]
        while i > 0:
            self.table[i] += diff
            i //= 2

    def sumRange(self, left: int, right: int) -> int:
        lo = self.offset + left
        hi = self.offset + right
        res = 0
        while lo < hi:
            if lo % 2 == 1:
                res += self.table[lo]
                lo = (lo + 1) // 2
            else:
                lo //= 2

            if hi % 2 == 0:
                res += self.table[hi]
                hi = (hi - 1) // 2
            else:
                hi //= 2

        return res + (self.table[lo] if lo == hi else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

def verify(ops, args, expecteds):
    numArray = NumArray(*args[0])
    for op, arg, expected in zip(ops, args, expecteds):
        res = None
        if op == 'sumRange':
            res = numArray.sumRange(*arg)
        elif op == 'update':
            res = numArray.update(*arg)
        assert expected == res


verify(["NumArray", "sumRange", "sumRange", "sumRange", "update", "update", "update", "sumRange", "update", "sumRange", "update"],
       [[[0, 9, 5, 7, 3]], [4, 4], [2, 4], [3, 3], [4, 5], [1, 7], [0, 8], [1, 2], [1, 9], [4, 4], [3, 4]],
       [None, 3, 15, 7, None, None, None, 12, None, 5, None])
verify(["NumArray", "sumRange", "update", "sumRange"], [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]], [None, 9, None, 8])
