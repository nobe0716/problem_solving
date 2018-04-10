class Solution(object):
    def monotoneIncreasingDigits(self, N):
        t = str(N)
        v, p = t[0], 0

        l = len(t)
        for i in range(l):
            if v > t[i]: # found decreasing spot
                break
            if t[i] != v:
                v = t[i]
                p = i
        # p += 1
        if p + 1 == l:  # is already monotone increasing
            return N

        a = str(int(t[:p + 1]) - 1)      # -1 from first group
        b = '9' * (l - (p + 1))                             # second group consist of (l - (p + 1)) 9s

        return int(a + b)

s = Solution()
print (s.monotoneIncreasingDigits(1234))
print (s.monotoneIncreasingDigits(100))
print (s.monotoneIncreasingDigits(332))
print (s.monotoneIncreasingDigits(120))
# print (s.monotoneIncreasingDigits(807))
print (s.monotoneIncreasingDigits(111))


