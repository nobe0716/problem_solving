from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0

        u = d = 0
        r = 0

        for i in range(1, len(arr)):
            if d and arr[i] > arr[i - 1] or arr[i] == arr[i - 1]:
                u = d = 0
            if arr[i] > arr[i - 1]:
                u += 1
            if arr[i] < arr[i - 1]:
                d += 1

            if u and d:
                r = max(r, u + d + 1)

        return r


s = Solution()
assert s.longestMountain(arr=[0, 2, 0, 2, 1, 2, 3, 4, 4, 1]) == 3
assert s.longestMountain(arr=[0, 1, 0]) == 3
assert s.longestMountain(arr=[2, 1, 4, 7, 3, 2, 5]) == 5
assert s.longestMountain(arr=[2, 2, 2]) == 0
