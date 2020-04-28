from typing import List


class Node:
    def __init__(self, num: int):
        self.prev = None
        self.next = None
        self.num = num

    def __repr__(self):
        return 'Node({}, prev: {}, next: {})'.format(self.num, self.prev, self.next)

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head = None
        self.tail = None
        self.num_to_node = {}
        for e in nums:
            self.add(e)

    def showFirstUnique(self) -> int:
        return self.head.num if self.head else -1

    def add(self, value: int) -> None:
        if value not in self.num_to_node:
            node = self.num_to_node[value] = Node(value)
            if not self.head:
                self.head = self.tail = node
            else:
                self.tail.next, node.prev = node, self.tail
                self.tail = node
        else:
            node = self.num_to_node[value]
            if node is self.head and node is self.tail:
                self.head = self.tail = None
            elif node is self.head:
                self.head = node.next
                node.next = None
            elif node is self.tail:
                self.tail = node.prev
                node.prev = None
            elif node.prev and node.next:
                node.prev.next, node.next.prev = node.next, node.prev
                node.prev = node.next = None


def test(a, b):
    obj = FirstUnique(b[0][0])
    r = [None]
    for command, param in zip(a[1:], b[1:]):
        if command == "showFirstUnique":
            r.append(obj.showFirstUnique())
        else:
            r.append(obj.add(param[0]))

    return r


# a = ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"]
# b = [[[2, 3, 5]], [], [5], [], [2], [], [3], []]
#
# print(test(a, b))

a = ["FirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique"]
b = [[[7, 7, 7, 7, 7, 7]], [], [7], [3], [3], [7], [17], []]
assert test(a, b) == [None, -1, None, None, None, None, None, 17]
