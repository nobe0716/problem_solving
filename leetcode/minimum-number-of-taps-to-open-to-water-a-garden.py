import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        heaps = defaultdict(list)
        dup_checker = defaultdict(set)
        for i, l in enumerate(ranges):
            if not l:
                continue

            key = min(n, i + l)
            value = max(0, i - l)

            if value not in dup_checker[key]:
                dup_checker[key].add(value)
                heapq.heappush(heaps[key], value)

        i = n + 1
        j = n
        num_of_taps = 0
        while j and any(heaps[_] for _ in range(j, i)):
            i, j = j, min(heaps[_][0] for _ in range(j, i) if heaps[_])
            num_of_taps += 1
        return num_of_taps if j == 0 else -1


s = Solution()
assert s.minTaps(n=7, ranges=[1, 2, 1, 0, 2, 1, 0, 1]) == 3
assert s.minTaps(n=5, ranges=[3, 4, 1, 1, 0, 0]) == 1
assert s.minTaps(n=3, ranges=[0, 0, 0, 0]) == -1
assert s.minTaps(n=8, ranges=[4, 0, 0, 0, 0, 0, 0, 0, 4]) == 2
assert s.minTaps(n=8, ranges=[4, 0, 0, 0, 4, 0, 0, 0, 4]) == 1
