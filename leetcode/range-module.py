import bisect


class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        il, ir = bisect.bisect_left(self.ranges, left), bisect.bisect_right(self.ranges, right)

        self.ranges[il:ir] = [left] * (il % 2 == 0) + [right] * (ir % 2 == 0)

    def queryRange(self, left: int, right: int) -> bool:
        il, ir = bisect.bisect_right(self.ranges, left), bisect.bisect_left(self.ranges, right)
        return il == ir and il % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        il, ir = bisect.bisect_left(self.ranges, left), bisect.bisect_right(self.ranges, right)
        self.ranges[il:ir] = [left] * (il % 2 == 1) + [right] * (ir % 2 == 1)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)


# Your RangeModule object will be instantiated and called as such:

obj = RangeModule()


def test(ops, args):
    obj.__init__()
    res = [None]
    for op, arg in zip(ops[1:], args[1:]):
        if op == 'addRange':
            res.append(obj.addRange(*arg))
        elif op == 'removeRange':
            res.append(obj.removeRange(*arg))
        elif op == 'queryRange':
            res.append(obj.queryRange(*arg))
    print(res)
    return res


assert test(
    ops=["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"],
    args=[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
) == [None, None, None, True, False, True]

assert test(
    ["RangeModule", "addRange", "removeRange", "removeRange", "addRange", "removeRange", "addRange", "queryRange",
     "queryRange", "queryRange"]
    , [[], [6, 8], [7, 8], [8, 9], [8, 9], [1, 3], [1, 8], [2, 4], [2, 9], [4, 6]]
) == [None, None, None, None, None, None, None, True, True, True]

assert test(
    ops=["RangeModule", "addRange", "addRange", "addRange", "queryRange", "queryRange", "queryRange", "removeRange",
         "queryRange"],
    args=[[], [10, 180], [150, 200], [250, 500], [50, 100], [180, 300], [600, 1000], [50, 150], [50, 100]]
) == [None, None, None, None, True, False, False, None, False]

assert test(
    ["RangeModule", "addRange", "addRange", "removeRange", "queryRange", "queryRange", "removeRange", "removeRange",
     "removeRange", "removeRange", "removeRange", "queryRange", "removeRange", "addRange", "removeRange", "addRange",
     "queryRange", "queryRange", "addRange", "addRange", "queryRange", "removeRange", "queryRange", "addRange",
     "queryRange", "removeRange", "removeRange", "addRange", "addRange", "removeRange", "removeRange", "removeRange",
     "addRange", "addRange", "queryRange", "queryRange", "queryRange", "queryRange", "queryRange", "removeRange",
     "removeRange", "queryRange", "addRange", "addRange", "addRange", "queryRange", "addRange", "addRange",
     "removeRange", "addRange", "queryRange", "removeRange", "addRange", "queryRange", "addRange", "addRange",
     "addRange", "queryRange", "addRange", "queryRange", "removeRange", "removeRange", "removeRange", "removeRange",
     "queryRange", "removeRange", "queryRange", "queryRange", "removeRange", "queryRange", "addRange", "addRange",
     "queryRange", "removeRange", "removeRange", "queryRange", "addRange", "removeRange", "removeRange", "addRange",
     "addRange", "addRange", "queryRange", "queryRange", "addRange", "queryRange", "removeRange", "queryRange",
     "removeRange", "addRange", "queryRange"],
    [[], [55, 62], [1, 29], [18, 49], [6, 98], [59, 71], [40, 45], [4, 58], [57, 69], [20, 30], [1, 40], [73, 93],
     [32, 93], [38, 100], [50, 64], [26, 72], [8, 74], [15, 53], [44, 85], [10, 71], [54, 70], [10, 45], [30, 66],
     [47, 98], [1, 7], [44, 78], [31, 49], [62, 63], [49, 88], [47, 72], [8, 50], [49, 79], [31, 47], [54, 87],
     [77, 78], [59, 100], [8, 9], [50, 51], [67, 93], [25, 86], [8, 92], [31, 87], [90, 95], [28, 56], [10, 42],
     [27, 34], [75, 81], [17, 63], [78, 90], [9, 18], [51, 74], [20, 54], [35, 72], [2, 29], [28, 41], [17, 95],
     [73, 75], [34, 43], [57, 96], [51, 72], [21, 67], [40, 73], [14, 26], [71, 86], [34, 41], [10, 25], [27, 68],
     [18, 32], [30, 31], [45, 61], [64, 66], [18, 93], [13, 21], [13, 46], [56, 99], [6, 93], [25, 36], [27, 88],
     [82, 83], [30, 71], [31, 73], [10, 41], [71, 72], [9, 56], [22, 76], [38, 74], [2, 77], [33, 61], [74, 75],
     [11, 43], [27, 75]]
) == [None, None, None, None, False, False, None, None, None, None, None, False, None, None, None, None, False, False,
      None, None, True, None, False, None, False, None, None, None, None, None, None, None, None, None, True, True,
      False, False, True, None, None, False, None, None, None, True, None, None, None, None, False, None, None, False,
      None, None, None, True, None, True, None, None, None, None, False, None, False, False, None, False, None, None,
      False, None, None, False, None, None, None, None, None, None, True, True, None, True, None, False, None, None,
      False]
