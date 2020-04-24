class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

    def __repr__(self):
        return '({}/{})'.format(self.key, self.value)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def reorder(self, node: Node):
        if node is self.head and node is self.tail:
            return
        elif node is self.head:
            self.head = self.head.next
            self.head.previous = None
            node.previous, node.next = self.tail, None
            self.tail.next = node
            self.tail = node
        elif node is not self.tail:
            node.previous.next, node.next.previous = node.next, node.previous
            node.previous, node.next = self.tail, None
            self.tail.next = node
            self.tail = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.reorder(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.reorder(self.cache[key])
            return
        elif not self.cache:  # init
            self.head = self.tail = self.cache[key] = Node(key, value)
        else:
            node = self.cache[key] = Node(key, value)
            self.tail.next, node.previous = node, self.tail
            self.tail = node

            if len(self.cache) > self.capacity:
                del self.cache[self.head.key]
                self.head = self.head.next
                self.head.previous = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def test(ops, params):
    lru_cache = LRUCache(params[0][0])
    r = [None]
    for method, param in zip(ops[1:], params[1:]):
        if method == 'put':
            lru_cache.put(*param)
            r.append(None)
        else:
            v = lru_cache.get(param[0])
            r.append(v)
    return r


ops = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
       "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
       "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
       "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
       "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
       "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
       "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
params = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
          [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11],
          [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5],
          [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22],
          [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29],
          [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27],
          [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7],
          [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
test(ops, params)


# ops = ["LRUCache","put","get","put","get","get"]
# params = [[1],[2,1],[2],[3,2],[2],[3]]
# test(ops, params)

ops = ["LRUCache", "put", "put", "put", "put", "get", "get", "get", "get", "put", "get", "get", "get", "get", "get"]
params = [[3], [1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2], [1], [5, 5], [1], [2], [3], [4], [5]]
r = test(ops, params)
print(r)
assert r == [None, None, None, None, None, 4, 3, 2, -1, None, -1, 2, 3, -1, 5]
