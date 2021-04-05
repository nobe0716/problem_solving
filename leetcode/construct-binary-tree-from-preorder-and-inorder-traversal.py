from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        val = preorder.pop(0)
        index = inorder.index(val)
        return TreeNode(val, self.buildTree(preorder, inorder[:index]), self.buildTree(preorder, inorder[index + 1:]))
