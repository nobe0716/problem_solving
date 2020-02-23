from operator import itemgetter
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=itemgetter(1))
        occupied = [False] * 100_001
        count = 0
        for event in events:
            for i in range(event[0], event[1] + 1):
                if not occupied[i]:
                    occupied[i] = True
                    count += 1
                    break
        return count


s = Solution()
assert s.maxEvents([[1, 5], [1, 5], [1, 5], [2, 3], [2, 3]]) == 5
assert s.maxEvents([[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]) == 5
assert s.maxEvents(events=[[1, 2], [2, 3], [3, 4]]) == 3
assert s.maxEvents(events=[[1, 2], [2, 3], [3, 4], [1, 2]]) == 4
assert s.maxEvents(events=[[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]) == 4
assert s.maxEvents(events=[[1, 100000]]) == 1
assert s.maxEvents(events=[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]) == 7
