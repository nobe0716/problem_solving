# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode()]

        res = []
        for left_count in range(1, N, 2):
            right_count = N - 1 - left_count
            if right_count < 1:
                continue

            left_trees = self.allPossibleFBT(left_count)
            right_trees = self.allPossibleFBT(right_count)

            for left in left_trees:
                for right in right_trees:
                    res.append(TreeNode(left=left, right=right))
        return res
