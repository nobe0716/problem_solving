import bisect
from operator import itemgetter
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        starts = list(map(itemgetter(0), intervals))
        ends = list(map(itemgetter(1), intervals))

        start_idx = bisect.bisect_left(ends, newInterval[0])
        end_idx = bisect.bisect_right(starts, newInterval[1])

        len_of_intervals = len(intervals)
        if start_idx == len_of_intervals:
            return intervals + [newInterval]
        if end_idx == 0:
            return [newInterval] + intervals
        prefix = intervals[:start_idx] if start_idx else []
        postfix = intervals[end_idx:] if end_idx < len_of_intervals else []

        mid = [min(starts[start_idx], newInterval[0]), max(ends[end_idx - 1], newInterval[1])]
        return prefix + [mid] + postfix


s = Solution()
assert s.insert(intervals=[[1, 5]], newInterval=[6, 8]) == [[1, 5], [6, 8]]
assert s.insert(intervals=[[3, 5]], newInterval=[1, 2]) == [[1, 2], [3, 5]]

assert s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [[1, 5], [6, 9]]
assert s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]) \
       == [[1, 2], [3, 10], [12, 16]]
assert s.insert(intervals=[], newInterval=[5, 7]) == [[5, 7]]
assert s.insert(intervals=[[1, 5]], newInterval=[2, 3]) == [[1, 5]]
assert s.insert(intervals=[[1, 5]], newInterval=[2, 7]) == [[1, 7]]
assert s.insert(intervals=[[2, 6]], newInterval=[1, 5]) == [[1, 6]]
