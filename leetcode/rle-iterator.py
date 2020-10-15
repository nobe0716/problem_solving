from collections import deque
from typing import List


class RLEIterator:

    def __init__(self, A: List[int]):
        self.deq = deque()
        for i in range(0, len(A), 2):
            if not A[i]:
                continue

            self.deq.append([A[i], A[i + 1]])

    def next(self, n: int) -> int:
        while self.deq and self.deq[0][0] < n:
            n -= self.deq[0][0]
            self.deq.popleft()

        if not self.deq:
            return -1
        self.deq[0][0] -= n
        return self.deq[0][1]


def proc(ops, args):
    s = RLEIterator(args[0][0])
    r = []
    for op, arg in zip(ops[1:], args[1:]):
        if op == 'next':
            r.append(s.next(arg[0]))
    return r


r = proc(["RLEIterator", "next", "next", "next", "next"], [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]])
print(r)
