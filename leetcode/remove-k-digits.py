class Solution(object):
    def removeKdigits(self, num, k):
        num = list(num)
        l = len(num)
        if k >= l:
            return "0"
        for i in range(k):
            j = 0
            while j < l - 1:
                if num[j] > num[j + 1]:
                    break
                j += 1
            num.pop(j)
            l -= 1
        return str(int(''.join(num)))
