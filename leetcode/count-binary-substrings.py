class Solution:
    def countBinarySubstrings(self, s):
        l = len(s)
        c = 0
        for i in range(l - 1):
            if s[i:i + 2] == '01' or s[i:i + 2] == '10':
                j = i + 1
                k = 0
                while 0 <= i - k and i + 1 + k < l and s[i - k] == s[i] and s[i + 1 + k] == s[i + 1]:
                    k += 1
                c += k
        return c
