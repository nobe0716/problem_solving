class Solution(object):
    def splitArray(self, nums, m):
        def validate(v: int) -> int:
            group_count = 1
            group_sum = 0
            for e in nums:
                if group_sum + e > v:
                    group_count += 1
                    group_sum = 0
                group_sum += e

            return group_count <= m

        lo, hi = max(nums), sum(nums)
        res = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if validate(mid):
                res = min(res, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return res


s = Solution()
assert s.splitArray([7, 2, 5, 10, 8], 2) == 18
assert s.splitArray(nums=[1, 2, 3, 4, 5], m=2) == 9
assert s.splitArray(nums=[1, 4, 4], m=3) == 4
assert s.splitArray([1, 2147483647], 2) == 2147483647
