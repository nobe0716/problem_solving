# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []
        heads = self.delNodes(root.left, to_delete) + self.delNodes(root.right, to_delete)
        if root.val in to_delete:
            return heads
        heads.append(root)

        if root.left and root.left.val in to_delete:
            root.left = None
        if root.right and root.right.val in to_delete:
            root.right = None
        for child in [root.left, root.right]:
            if child in heads:
                heads.remove(child)
        return heads
