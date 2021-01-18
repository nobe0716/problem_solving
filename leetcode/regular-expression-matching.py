from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls = len(s)
        lp = len(p)

        @lru_cache(None)
        def back(i, j):
            if i == ls and j == lp:
                return True
            if j == lp:
                return False
            if i == ls:
                return j + 1 < lp and p[j + 1] == '*' and back(i, j + 2)
            if p[j:j + 2] == '.*':
                return any(back(k, j + 2) for k in range(i, ls + 1))
            if j + 1 < lp and p[j + 1] == '*':
                if s[i] == p[j]:
                    for k in range(i + 1, ls + 1):
                        if back(k, j + 2):
                            return True
                        if k < ls and s[k] != s[i]:
                            break
                return back(i, j + 2)
            return (s[i] == p[j] or p[j] == '.') and back(i + 1, j + 1)

        return back(0, 0)


s = Solution()
assert s.isMatch("ab", ".*..")
assert not s.isMatch("a", "ab*a")
assert not s.isMatch("aaa", "ab*a")
assert not s.isMatch("ab", ".*c")
assert not s.isMatch('aa', 'a')
assert s.isMatch('aa', 'a*')
assert s.isMatch('ab', '.*')
assert s.isMatch('aab', 'c*a*b')
assert not s.isMatch(s="mississippi", p="mis*is*p*.")
assert s.isMatch("ababbb", "a.abbb")
assert s.isMatch("ababbb", "a.abbbc*")
