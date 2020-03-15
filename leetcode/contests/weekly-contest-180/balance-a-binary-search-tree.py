# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def collect(node: TreeNode):
            if not node:
                return []
            return [node.val] + collect(node.left) + collect(node.right)

        def compose_node(vals: List[int]):
            if not vals:
                return None
            if len(vals) == 1:
                return TreeNode(vals[0])
            pivot_idx = len(vals) // 2
            left_vals, pivot_val, right_vals = vals[:pivot_idx], vals[pivot_idx], vals[pivot_idx + 1:]
            node = TreeNode(pivot_val)
            node.left = compose_node(left_vals)
            node.right = compose_node(right_vals)
            return node

        values = sorted(collect(root))
        return compose_node(values)
