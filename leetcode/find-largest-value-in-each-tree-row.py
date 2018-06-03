# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        def helper(root, depth, res):
            if root is None:
                return None
            if depth > len(res):
                res.append(root.val)
            res[depth - 1] = max(res[depth - 1], root.val)

            helper(root.left, depth + 1, res)
            helper(root.right, depth + 1, res)

        res = []
        helper(root, 1, res)
        return res


