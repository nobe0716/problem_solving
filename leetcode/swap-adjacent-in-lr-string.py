class Solution(object):
    def canTransform(self, start, end):
        s = set(['XL', 'RX'])
        start, end = list(start), list(end)
        l = len(start)
        for i in range(l):
            while start[i] != end[i]:
                j = i + 1
                while j < l  and start[j] != end[i]:
                    j += 1
                if j >= l:
                    return False
                while j > i:
                    if "".join(start[j-1:j+1]) in s:
                        start[j - 1], start[j] = start[j], start[j - 1]
                        j -= 1
                    else:
                        return False
        return True