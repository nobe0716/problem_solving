from collections import Counter


class MyCalendarThree:

    def __init__(self):
        self.c = Counter()

    def book(self, start: int, end: int) -> int:
        self.c[start] += 1
        self.c[end] -= 1
        r = s = 0
        for k, v in sorted(self.c.items()):
            s += v
            r = max(r, s)
        return r

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
