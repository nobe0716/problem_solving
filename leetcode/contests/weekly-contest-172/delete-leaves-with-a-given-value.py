# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root.left:
            self.removeLeafNodes(root.left, target)
            if root.left.val == target and not root.left.left and not root.left.right:
                root.left = None
        if root.right:
            self.removeLeafNodes(root.right, target)
            if root.right.val == target and not root.right.left and not root.right.right:
                root.right = None
        if root.val == target and root.left is None and root.right is None:
            return None
        return root
