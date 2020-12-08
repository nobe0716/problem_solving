from collections import deque
from typing import List

from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = SortedList()
        res = deque()
        for e in nums[::-1]:
            res.appendleft(len(sorted_list) - sorted_list.bisect_right(-e))
            sorted_list.add(-e)
        return list(res)


s = Solution()
assert s.countSmaller(nums=[5, 2, 6, 1]) == [2, 1, 1, 0]
