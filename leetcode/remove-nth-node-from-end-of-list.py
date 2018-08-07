class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getNthFromEnd(self, prev, head, n):
        if head.next is None:
            return [prev, head, 1]
        else:
            r_prev, node, idx = self.getNthFromEnd(head, head.next, n)
            if idx == n:
                return r_prev, node, idx
            else:
                return prev, head, idx + 1

    def removeNthFromEnd(self, head, n):
        prev, node, idx = self.getNthFromEnd(None, head, n)
        #print (prev, node, idx)
        if prev:
            prev.next = node.next if node else None
        else:
            head = head.next
        return head
