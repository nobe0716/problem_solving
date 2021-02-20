from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        """
                initialize your data structure here.
                """
        self.v = SortedList()

    def addNum(self, num: int) -> None:
        self.v.add(num)

    def findMedian(self) -> float:
        l = len(self.v)
        if l % 2 == 1:
            return self.v[l // 2]
        return (self.v[l // 2 - 1] + self.v[l // 2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

def validate(ops, args, expected):
    obj = MedianFinder()
    res = [None]
    for op, arg in zip(ops[1:], args[1:]):
        if op == "addNum":
            res.append(obj.addNum(arg[0]))
        else:
            res.append(obj.findMedian())
    assert res == expected


validate(ops=["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
         args=[[], [-1], [], [-2], [], [-3], [], [-4], [], [-5], []],
         expected=[None, None, -1.00000, None, -1.50000, None, -2.00000, None, -2.50000, None, -3.00000])
