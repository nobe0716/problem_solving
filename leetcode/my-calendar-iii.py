"""
## Name of Prob

## Link
https://leetcode.com/problems/my-calendar-iii/

## Note

Reservation representation start, end means [start, end), half opened

## Input
book intervals

## Output
the maximum duplicates of current book

## Strategy

Number of duplicates at position i is calculated difference between 'the number of books has been made before i' and
'the number of book has been terminated before i'.
So we can calculate it on sorted counter map
"""
from collections import Counter


class MyCalendarThree:

    def __init__(self):
        self._counter = Counter()
        # self._max = 0

    def book(self, start: int, end: int) -> int:
        self._counter[start] += 1
        self._counter[end] -= 1

        max_c = 0
        c = 0
        for k in sorted(self._counter.keys()):
            v = self._counter[k]
            c += v
            max_c = max(max_c, c)
        return max_c


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)


# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarThree()
expected_res = [1, 1, 2, 3, 3, 3]
book_intervals = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]

label = ["MyCalendarThree", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book",
         "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book",
         "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book",
         "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book",
         "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book",
         "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book"]
books = [[], [28, 36], [9, 16], [71, 79], [37, 43], [88, 94], [22, 29], [95, 100], [1, 7], [40, 48], [31, 39], [5, 12],
         [92, 100], [54, 59], [33, 41], [2, 7], [16, 25], [57, 66], [56, 61], [63, 68], [88, 93], [99, 100], [56, 65],
         [5, 13], [35, 42], [69, 74], [46, 51], [39, 44], [28, 36], [78, 87], [70, 79], [91, 99], [11, 19], [41, 46],
         [78, 87], [67, 73], [22, 31], [4, 10], [31, 40], [54, 62], [69, 76], [36, 41], [78, 84], [40, 46], [10, 18],
         [4, 11], [75, 84], [86, 94], [32, 40], [34, 39], [90, 99], [8, 13], [85, 93], [24, 29], [10, 17], [10, 18],
         [8, 17], [1, 9], [36, 45], [42, 50], [92, 97], [22, 29], [62, 67], [70, 77], [77, 86], [74, 81], [73, 78],
         [47, 52], [73, 80], [24, 29], [69, 75], [69, 77], [3, 9], [34, 41], [22, 27], [3, 9], [79, 88], [34, 40],
         [49, 56], [42, 48], [43, 52]]
for idx, pos in enumerate(books[1:]):
    start, end = pos
    book_result = obj.book(start, end)
    print(book_result, start, end)
    # assert book_result == expected_res[idx]
    # assert expected_res[idx] == book_result
