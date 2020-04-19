from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l: int, r: int):
            if l == r:
                return l if nums[l] == target else -1
            p = (l + r) // 2
            if nums[p] == target:
                return p

            if nums[l] <= nums[p]:
                if nums[l] <= target < nums[p]:
                    return bs(l, p - 1)
                else:
                    return bs(p + 1, r)
            elif nums[l] > nums[p]:
                if nums[p] < target <= nums[r]:
                    return bs(p + 1, r)
                else:
                    return bs(l, p - 1)

        if not nums:
            return -1
        return bs(0, len(nums) - 1)


s = Solution()
assert s.search([1, 3], 0) == -1
assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
