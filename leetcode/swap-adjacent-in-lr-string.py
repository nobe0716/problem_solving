class Solution(object):
    def canTransform(self, start, end):
        start, end = list(start), list(end)
        trans = {'XL', 'RX'}
        stop = len(start)
        for i in range(stop):
            if start[i] == end[i]:
                continue
            j = i + 1
            while j < stop and start[j] != end[i]:
                j += 1
            if j == stop:
                return False
            while j > i:
                if (start[j - 1] + start[j]) in trans:
                    start[j - 1], start[j] = start[j], start[j - 1]
                    j -= 1
                else:
                    return False
        return True


s = Solution()
assert s.canTransform("RXXLRXRXL", "XRLXXRRLX")
