# Definition for a binary tree node.
from typing import Callable


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def get_height(node: TreeNode, func: Callable[[TreeNode], TreeNode]) -> int:
            height = 0
            while node:
                height += 1
                node = func(node)
            return height

        lh = get_height(root, lambda node: node.left)
        rh = get_height(root, lambda node: node.right)

        if lh == rh:
            return 2 ** lh - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
