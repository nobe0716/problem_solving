# Definition for singly-linked list.
from random import Random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        self.length = 0
        self.head = head
        self.rand = Random()
        node = head
        while node:
            node = node.next
            self.length += 1

    def getRandom(self) -> int:
        p = self.rand.randrange(0, self.length)
        node = self.head
        for _ in range(p):
            node = node.next

        return node.val
