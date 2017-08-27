# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):

    def findLast(self, root, height, idx):
        if height == 0:
            return idx
        left_idx = right_idx = 0
        if root.right is not None:
            right_idx = self.findLast(self, root.right, height - 1, idx * 2 + 1)
        if root.left is not None:
            left_idx = self.findLast(self, root.left, height - 1, idx * 2)
        return max([left_idx, right_idx])

    def countNodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        # calc height
        node = root
        h = 0
        while node is not None:
            h += 1
            node = node.left

        # find last node
        return self.findLast(root, h, 1)


