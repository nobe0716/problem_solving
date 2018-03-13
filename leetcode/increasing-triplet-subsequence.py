class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False

        min_v = nums[0]
        mid_v = None

        for n in nums[1:]:
            if mid_v is not None and n > mid_v:
                return True
            if n > min_v and (mid_v is None or mid_v > n):
                mid_v = n
            elif n < min_v:
                min_v = n
                #print min_v, mid_v
        return False
        