import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.idx = list(range(0, len(nums)))

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.idx)
        return [self.nums[i] for i in self.idx]