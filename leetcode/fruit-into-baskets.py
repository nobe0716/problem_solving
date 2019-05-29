"""
## Name of Prob
904. Fruit Into Baskets

## Link
https://leetcode.com/problems/fruit-into-baskets/

## Note
find longest sub-sequence that is consist of two num

## Input
num array

len(arr) <= 40_000 ; should be solved faster than O(N^2)
each num is less than length, bound to 40_000

## Output
maximum number of fruits can be collected

## Strategy

Hold start index of two-fruit and one-fruit individually.
"""
from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        len_of_tree = len(tree)
        if len_of_tree <= 2:
            return len_of_tree

        current_two_fruit = {tree[0]}
        start_index_two_fruit = 0
        start_index_one_fruit = 0
        max_len = 0
        for i in range(1, len_of_tree):
            cur_fruit = tree[i]

            if cur_fruit not in current_two_fruit:
                if len(current_two_fruit) < 2:
                    current_two_fruit.add(cur_fruit)
                else:
                    current_two_fruit = {tree[i - 1], cur_fruit}
                    max_len = max(max_len, i - start_index_two_fruit)
                    start_index_two_fruit = start_index_one_fruit

            if cur_fruit != tree[i - 1]:
                start_index_one_fruit = i

        return max(max_len, len_of_tree - start_index_two_fruit)


s = Solution()
assert s.totalFruit([1, 2, 1]) == 3
assert s.totalFruit([1, 2, 3, 2, 2]) == 4
assert s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
assert s.totalFruit([1, 0, 3, 4, 3]) == 3
