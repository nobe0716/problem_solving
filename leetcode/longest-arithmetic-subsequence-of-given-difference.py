from collections import defaultdict
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        t = defaultdict(int)
        for e in arr:
            t[e] = t[e - difference] + 1

        return max(t.values())


s = Solution()
assert s.longestSubsequence([1, 2, 3, 4], 1) == 4
assert s.longestSubsequence(arr=[1, 3, 5, 7], difference=1) == 1
assert s.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2) == 4
