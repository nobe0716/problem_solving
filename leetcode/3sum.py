class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        nums = list(sorted(nums))
        l = len(nums)
        r = set()

        u = set()
        d = {}

        for i in range(l - 1, -1, -1):
            if nums[i] not in d:
                d[nums[i]] = i

        for i in range(l - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, l):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                v = nums[i] + nums[j]
                if -v in d and d[-v] > j:
                    r.add((nums[i], nums[j], -v))

        return list(map(list, r))