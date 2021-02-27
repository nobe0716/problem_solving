# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
from functools import lru_cache


class MountainArray:
    def __init__(self, arr):
        self.array = arr

    def get(self, index: int) -> int:
        assert 0 <= index < len(self.array)
        return self.array[index]

    def length(self) -> int:
        return len(self.array)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        @lru_cache(None)
        def get_height(index: int) -> int:
            return mountain_arr.get(index)

        # found top
        lo, hi = 1, length - 2
        top = None
        while lo <= hi and not top:
            mid = (lo + hi) // 2

            a, b, c = get_height(mid - 1), get_height(mid), get_height(mid + 1)
            if a < b > c:
                top = mid
            elif a < b < c:
                lo = mid + 1
            else:
                hi = mid - 1

        if get_height(top) == target:
            return top
        # bs left

        lo, hi = 0, top - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            v = get_height(mid)
            if v == target:
                return mid
            if v > target:
                hi = mid - 1
            else:
                lo = mid + 1

        # bs right
        lo, hi = top + 1, length - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            v = get_height(mid)
            if v == target:
                return mid
            if v > target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


s = Solution()
assert s.findInMountainArray(1, MountainArray([0, 5, 3, 1])) == 3
assert s.findInMountainArray(0, MountainArray([3, 5, 3, 2, 0])) == 4
