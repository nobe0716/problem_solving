class Solution(object):
    def maximumSwap(self, num):
        l = len(str(num))
        if l == 1:
            return num
        v = num
        num = list(str(num))
        for i in range(l - 1):
            for j in range(i + 1, l):
                num[i], num[j] = num[j], num[i]
                v = max(v, int(''.join(num)))
                num[i], num[j] = num[j], num[i]
        return v
