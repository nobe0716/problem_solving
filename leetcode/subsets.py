from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        use = [False] * 10

        def back(i: int):
            if i == n:
                subset = []
                for j in range(n):
                    if use[j]:
                        subset.append(nums[j])
                subsets.append(subset)
                return
            for v in [False, True]:
                use[i] = v
                back(i + 1)

        back(0)
        return subsets
