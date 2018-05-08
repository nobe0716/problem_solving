class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        new_head = RandomListNode(head.label)
        prev = head
        cur = new_head
        d = {}
        while prev is not None:
            if prev.next is not None:
                if prev.next.label not in d:
                    node = RandomListNode(prev.next.label)
                    d[prev.next.label] = node
                else:
                    node = d[prev.next.label]
                cur.next = node
            if prev.random is not None:
                if prev.random.label not in d:
                    node = RandomListNode(prev.random.label)
                    d[prev.random.label] = node
                else:
                    node = d[prev.random.label]
                cur.random = node
            prev = prev.next
            cur = cur.next
        return new_head
