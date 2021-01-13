from typing import List

from sortedcontainers import SortedList


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        l = SortedList(nums[:k])
        medians = []
        if k % 2:
            medians.append(l[k // 2])
        else:
            medians.append((l[k // 2 - 1] + l[k // 2]) / 2.0)

        for i in range(k, len(nums)):
            l.remove(nums[i - k])
            l.add(nums[i])

            if k % 2:
                medians.append(l[k // 2])
            else:
                medians.append((l[k // 2 - 1] + l[k // 2]) / 2.0)
        return medians


s = Solution()
assert s.medianSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3) == [1, -1, -1, 3, 5, 6]
