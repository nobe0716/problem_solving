"""
## Name of Prob

## Link
https://leetcode.com/problems/my-calendar-ii/

## Note

Reservation representation start, end means [start, end), half opened

## Input

## Output

## Strategy

Collapse can be avoided for new comer [start, end). For pre-exist [x, y) x >= end and y <= start

if collapse occurs, save dup_booked interval

for next book, check dup_booked intervals first, and return False if any dup_booked has collapsed with new comer.
Then, check new comer with pre-exist books and add to dup_intervals if collapsed occurs

"""


class MyCalendarTwo:

    def __init__(self):
        self._intervals = list()
        self._dup_intervals = list()

    def book(self, start: int, end: int) -> bool:
        # print('int', self._intervals)
        # print('dup', self._dup_intervals)
        for x, y in self._dup_intervals:
            if x >= end or y <= start:
                continue
            return False

        for x, y in self._intervals:
            if x >= end or y <= start:
                continue
            self._dup_intervals.append((max(start, x), min(end, y)))
        self._intervals.append((start, end))

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
expected_res = [True, True, True, False, True, True]
book_intervals = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
for idx, pos in enumerate(book_intervals):
    start, end = pos
    book_result = obj.book(start, end)
    print(idx, start, end, book_result, expected_res[idx])
    assert book_result == expected_res[idx]
    # assert expected_res[idx] == book_result
