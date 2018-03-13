class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 1:
            return ''
        r = s[:1]
        i = 1
        l = len(s)
        for i in range(1, l):
            if s[i - 1] == s[i]:
                j, k = i - 1, i
                while 0 <= j and k < l and s[j] == s[k]:
                    j -= 1
                    k += 1
                if (k - j + -1) >= len(r):
                    r = s[j + 1:k]
            if s[i - 2] == s[i]:
                j, k = i - 2, i
                while 0 <= j and k < l and s[j] == s[k]:
                    j -= 1
                    k += 1
                if (k - j + -1) >= len(r):
                    r = s[j + 1:k]
        return r