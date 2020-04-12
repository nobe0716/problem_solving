# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def traverse(root: TreeNode) -> (int, int):
            if root is None:
                return (0, 0)
            l, r = traverse(root.left), traverse(root.right)
            # print(root.val, max(l[0], r[0], l[1] + r[1]), max(l[1], r[1]) + 1)
            return max(l[0], r[0], l[1] + r[1]), max(l[1], r[1]) + 1

        return traverse(root)[0]
