from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        return sum(1 if (e + 1) in s else 0 for e in arr)
