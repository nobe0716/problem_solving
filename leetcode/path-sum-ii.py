# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        def helper(root, cur, res, s):
            if root is None:
                return None

            cur.append(root.val)
            s -= root.val
            if root.left is None and root.right is None:
                if s == 0:
                    res.append(list(cur))
            else:
                helper(root.left, cur, res, s)
                helper(root.right, cur, res, s)
            cur.pop()

        res = []
        helper(root, [], res, sum)
        return res
