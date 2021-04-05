from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        pivot = [intervals[0][0], intervals[0][1]]
        for lo, hi in intervals[1:]:
            if lo <= pivot[1]:
                pivot[1] = max(pivot[1], hi)
            else:
                res.append(pivot)
                pivot = [lo, hi]
        res.append(pivot)
        return res


s = Solution()
assert s.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
