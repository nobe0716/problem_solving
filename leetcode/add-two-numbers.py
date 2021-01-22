# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def traverse(l1: ListNode, l2: ListNode, carry: int):
            if not l1 and not l2 and carry == 0:
                return None
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            carry, val = val // 10, val % 10

            return ListNode(val, traverse(l1.next if l1 else None, l2.next if l2 else None, carry))

        return traverse(l1, l2, 0)
