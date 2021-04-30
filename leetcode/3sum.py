from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()
        for i in range(0, len(nums)):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                b, c = nums[lo], nums[hi]
                if b + c == -a:
                    res.add((a, b, c))

                if b + c < -a:
                    lo += 1
                else:
                    hi -= 1

        res = list(map(list, res))
        # print(res)
        return res


s = Solution()
assert s.threeSum(nums=[-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
