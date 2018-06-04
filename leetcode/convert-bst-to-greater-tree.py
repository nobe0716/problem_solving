# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        def helper(root):
            if not root:
                return None
            helper(root.right)
            root.val += self.cur_sum
            self.cur_sum = root.val
            helper(root.left)

        self.cur_sum = 0
        helper(root)
        return root
