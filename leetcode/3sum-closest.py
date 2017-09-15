class Solution(object):
    def threeSumClosest(self, nums, target):
        l = len(nums)
        possible_sum_of_two_value = set() # store currently possible sum of two elements

        nearest_sum_of_three_value = None
        current_minimum_distance_to_target = float('inf')

        possible_sum_of_two_value.add(nums[0] + nums[1])
        for i in range(2, l):
            n = nums[i]
            for e in possible_sum_of_two_value:
                if e + n == target:
                    return target
                distance = abs(e + n - target)
                if distance < current_minimum_distance_to_target:
                    current_minimum_distance_to_target = distance
                    nearest_sum_of_three_value = e + n
            for p in nums[:i]:
                possible_sum_of_two_value.add(n + p)

        return nearest_sum_of_three_value

s = Solution()
print s.threeSumClosest([0,0,0], 1)
print s.threeSumClosest([-1,2,1,-4], 1)