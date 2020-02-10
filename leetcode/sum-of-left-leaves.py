# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def solve(node, from_left):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return node.val if from_left else 0
            return solve(node.left, True) + solve(node.right, False)

        return solve(root, False)
