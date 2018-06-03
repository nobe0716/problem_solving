# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        def helper(root, current_sum, res):
            if root is None:
                return None
            current_sum = current_sum * 10 + root.val
            if root.left is None and root.right is None:
                res.val += current_sum
            helper(root.left, current_sum, res)
            helper(root.right, current_sum, res)

        r = TreeNode(0)
        helper(root, 0, r)
        return r.val