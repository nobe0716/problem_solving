class Solution(object):
    def sortList(self, head):
        def merge(a, b):
            # print('merge ' + str(a.val) + ', ' + str(b.val))
            dummy_head = ListNode(None)
            node = dummy_head
            while a is not None and b is not None:
                if a.val < b.val:
                    node.next, a = a, a.next
                else:
                    node.next, b = b, b.next
                node = node.next
            while a is not None:
                node.next, a = a, a.next
                node = node.next
            while b is not None:
                node.next, b = b, b.next
                node = node.next
            return dummy_head.next

        if head is None or head.next is None:
            return head
        mid = head
        node = head
        while node is not None and node.next is not None and node.next.next is not None:
            mid = mid.next
            node = node.next.next
        node = mid.next
        mid.next = None
        return merge(self.sortList(head), self.sortList(node))
