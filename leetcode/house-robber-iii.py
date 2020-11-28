# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def proc(node: TreeNode):
            if not node:
                return (0, 0)
            lv, rv = map(proc, (node.left, node.right))
            return (node.val + lv[1] + rv[1], max(lv) + max(rv))

        return proc(root)
