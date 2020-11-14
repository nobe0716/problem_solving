# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        _NODE_VAL_NONE = -201
        tree_set = set()
        sol_set = set()
        dup_nodes = []

        def encode(v: List):
            return ','.join(map(str, v))

        def traverse(node: TreeNode):
            if not node:
                return [_NODE_VAL_NONE]
            v = [node.val] + traverse(node.left) + traverse(node.right)
            k = encode(v)
            if k in tree_set:
                if k not in sol_set:
                    dup_nodes.append(node)
                    sol_set.add(k)
            else:
                tree_set.add(k)
            return v

        traverse(root)
        if str(_NODE_VAL_NONE) in dup_nodes:
            dup_nodes.remove(str(_NODE_VAL_NONE))
        return dup_nodes
