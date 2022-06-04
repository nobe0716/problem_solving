import bisect


# takes 30 min to implement

class ExamRoom:

    def __init__(self, n: int):
        self.students = []
        self.n = n

    def seat(self) -> int:
        if len(self.students) == 0:
            self.students.append(0)
            return 0

        max_distance = self.students[0]
        max_pos = 0
        for lo, hi in zip(self.students, self.students[1:]):
            distance = (hi - lo) // 2
            if distance > max_distance:
                max_distance = distance
                max_pos = (lo + hi) // 2

        if self.n - 1 - self.students[-1] > max_distance:
            max_pos = self.n - 1

        bisect.insort(self.students, max_pos)
        return max_pos

    def leave(self, p: int) -> None:
        self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)


def test(ops, args, expects):
    obj = ExamRoom(args[0][0])

    result = [None]
    for op, arg in zip(ops[1:], args[1:]):
        if op == 'seat':
            v = obj.seat()
        else:
            obj.leave(arg[0])
            v = None
        result.append(v)
    print(result)
    print(expects)
    assert result == expects


test(["ExamRoom", "seat", "seat", "seat", "leave", "leave", "seat", "seat", "seat", "seat", "seat", "seat", "seat",
      "seat", "seat", "leave"],
     [[10], [], [], [], [0], [4], [], [], [], [], [], [], [], [], [], [0]],
     [None, 0, 9, 4, None, None, 0, 4, 2, 6, 1, 3, 5, 7, 8, None]
     )
