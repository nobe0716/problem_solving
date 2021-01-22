# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.dig_stack(root)

    def dig_stack(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        elem = self.stack.pop()
        if elem.right:
            self.dig_stack(elem.right)
        return elem.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
