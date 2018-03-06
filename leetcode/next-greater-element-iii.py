from collections import defaultdict
class Solution(object):
    def nextGreaterElement(self, n):
        c = defaultdict(int)
        res = "-1"
        while n > 0:
            d = n % 10
            n /= 10
            c[d] += 1
            v = None
            for i in range(d + 1, 10):
                if i in c:
                    v = i
                    break
            if v is not None:
                c[v] -= 1
                res = str(n) + str(v)
                for i in range(10):
                    if i in c:
                        res += str(i) * c[i]
                break
        if int(res) > 0x7FFFFFFF:
            return -1
        return int(res)