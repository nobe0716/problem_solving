class Solution(object):
    def isIsomorphic(self, s, t):
        s2t, t2s = {}, {}
        for si, ti in zip(s, t):
            if si not in s2t and ti not in t2s:
                s2t[si], t2s[ti] = ti, si
            elif si not in s2t or ti not in t2s:
                return False
            elif s2t[si] != ti or t2s[ti] != si:
                return False

        return True


s = Solution()
assert s.isIsomorphic(s="egg", t="add")
assert not s.isIsomorphic("badc", "baba")
assert not s.isIsomorphic("foo", "bar")
