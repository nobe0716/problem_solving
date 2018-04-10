class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if s == t == "":
            return True
        for _ in range(len(s) - 1):
            s = s[1:] + s[0]
            if s == t:
                return True
        return False