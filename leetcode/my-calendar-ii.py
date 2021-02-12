from sortedcontainers import SortedDict


class MyCalendarTwo:

    def __init__(self):
        self.books = SortedDict()

    def book(self, start: int, end: int) -> bool:
        if start not in self.books:
            self.books[start] = 0
        if end not in self.books:
            self.books[end] = 0

        self.books[start] += 1
        self.books[end] -= 1

        dups = 0
        for v in self.books.values():
            dups += v
            if dups >= 3:
                break

        if dups >= 3:
            self.books[start] -= 1
            self.books[end] += 1

            if self.books[start] == 0:
                del self.books[start]
            if self.books[end] == 0:
                del self.books[end]
            return False
        return True


def validate(ops, args):
    s = MyCalendarTwo()
    r = [None]
    for op, arg in zip(ops[1:], args[1:]):
        r.append(s.book(*arg))
    return r


assert validate(["MyCalendarTwo", "book", "book", "book", "book", "book", "book"],
                [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]) == [None, True, True, True, False, True, True]
