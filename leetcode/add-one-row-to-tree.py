# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        def connect(root, v, d):
            if d == 1:
                new_node = TreeNode(v)
                new_node.left = root
                return new_node
            elif d == 2:
                new_node = TreeNode(v)
                new_node.left = root.left
                root.left = new_node
                new_node = TreeNode(v)
                new_node.right = root.right
                root.right = new_node
                return root
            else:
                if root.left is not None:
                    connect(root.left, v, d - 1)
                if root.right is not None:
                    connect(root.right, v, d - 1)
                return root
        return connect(root, v, d)

