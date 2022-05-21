class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def divisible(s: str, t: str) -> bool:
            if len(t) == 0:
                return True
            if len(s) % len(t) != 0:
                return False
            for i in range(len(s)):
                if s[i] != t[i % len(t)]:
                    return False
            return True

        c = 0
        for a, b in zip(str1, str2):
            if a != b:
                break
            c += 1
        for i in range(c, -1, -1):
            tok = str1[:i]
            if divisible(str1, tok) and divisible(str2, tok):
                return tok
        return ""
