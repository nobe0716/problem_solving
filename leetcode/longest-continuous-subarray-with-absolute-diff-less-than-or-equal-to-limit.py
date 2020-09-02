from collections import Counter
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 1
        c = Counter([nums[0]])
        keys = [nums[0]]
        lo = 0

        for hi in range(1, len(nums)):
            e = nums[hi]
            if e in c:
                c[e] += 1
            else:
                while keys and (abs(keys[-1] - e) > limit or abs(keys[0] - e) > limit):
                    c[nums[lo]] -= 1
                    if c[nums[lo]] == 0:
                        keys.remove(nums[lo])
                        del c[nums[lo]]
                    lo += 1
                c[e] += 1
                keys.append(e)
                keys.sort()
            res = max(res, hi - lo + 1)
        return res


s = Solution()
assert s.longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0) == 3
assert s.longestSubarray([8, 2, 4, 7], 4) == 2
assert s.longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5) == 4
print('check finished')
