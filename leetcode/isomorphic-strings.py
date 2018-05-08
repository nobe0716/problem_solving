class Solution(object):
    def isIsomorphic(self, s, t):
        d, e = {}, {}
        for a, b in zip(s, t):
            if a in d and d[a] != b:
                return False
            d[a] = b
            if b in e and e[b] != a:
                return False
            e[b] = a
        return True
