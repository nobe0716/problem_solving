class Solution(object):
    def maxCount(self, m, n, ops):
        if len(ops) == 0:
            return m * n

        print min(ops, key=lambda x: x[0])
        print min(ops, key=lambda x: x[1])
        a = 400000
        b = 400000
        for op in ops:
            a = op[0] if op[0] < a else a
            b = op[1] if op[1] < b else b

        return a * b

s = Solution()
print s.maxCount(3, 3, [[2, 2], [3, 3]])


