# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        node = TreeNode(preorder[0])
        lt = list(filter(lambda x: x < preorder[0], preorder))
        gt = list(filter(lambda x: x > preorder[0], preorder))
        node.left = self.bstFromPreorder(lt)
        node.right = self.bstFromPreorder(gt)
        return node
