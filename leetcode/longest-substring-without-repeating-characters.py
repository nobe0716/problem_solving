class Solution:
    def lengthOfLongestSubstring(self, s):
        t = ''
        m = 0
        for ch in s:
            if ch in t:
                p = 0
                while p < len(t) and t[p] != ch:
                    p += 1
                t = t[p + 1:]
            t += ch
            m = max(m, len(t))
        return m
