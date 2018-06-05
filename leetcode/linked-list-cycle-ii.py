# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head is None:
            return head
        s = set()
        s.add(head)
        head = head.next
        while head is not None and head not in s:
            s.add(head)
            head = head.next
        return head
