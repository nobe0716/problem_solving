class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def find_middle(node: ListNode, cur: int):
            if node is None:
                return (None, 0)
            middle_node, remain_count = find_middle(node.next, cur + 1)
            if middle_node:
                return (middle_node, None)
            if cur == remain_count or cur == remain_count + 1:
                return (node, None)
            return (None, remain_count + 1)

        middle, remain = find_middle(head, 0)
        return middle
