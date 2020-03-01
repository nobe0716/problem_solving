# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def is_sub_path(head: ListNode, root: TreeNode):
            if not head:
                return True
            if not root or head.val != root.val:
                return False
            return is_sub_path(head.next, root.left) or is_sub_path(head.next, root.right)

        def traverse(head: ListNode, root: TreeNode):
            if not root:
                return False
            return (root.val == head.val and is_sub_path(head, root)) or traverse(head, root.left) or traverse(head,
                                                                                                               root.right)

        return traverse(head, root)
