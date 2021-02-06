# Definition for a binary tree node.
from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def traverse(node: TreeNode) -> Tuple[int, int]:
            l, r = traverse(node.left) if node.left else (0, float('-inf')), traverse(node.right) if node.right else (0, float('-inf'))

            local_maximum = max(l[0], r[0], 0) + node.val
            return local_maximum, max(max(0, l[0]) + max(0, r[0]) + node.val, l[1], r[1])

        return max(traverse(root))
