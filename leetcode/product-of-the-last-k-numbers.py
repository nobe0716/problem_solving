from collections import deque


class ProductOfNumbers:

    def __init__(self):
        self.q = deque([1])
        self.z = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.z = len(self.q)
            self.q.appendleft(1)
        else:
            self.q.appendleft(num * self.q[0])

    def getProduct(self, k: int) -> int:
        if len(self.q) - self.z <= k:
            return 0
        return self.q[0] // self.q[k]


s = ProductOfNumbers()


def verify(ops, params):
    r = []
    for op, param in zip(ops[1:], params[1:]):
        if op == 'add':
            r.append(s.add(param[0]))
        else:
            r.append(s.getProduct(param[0]))
    return r


print(verify(["ProductOfNumbers", "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add",
              "getProduct"], [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]))
