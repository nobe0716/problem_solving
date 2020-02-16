import functools


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        @functools.lru_cache(None)
        def is_match(s, p):
            if len(s) == 0 and len(p) == 0:
                return True
            if len(p) == 0:
                return False
            if len(s) == 0:
                return all(p[i] == '*' for i in range(len(p)))
            if p[0] == '*':
                return any(is_match(s[i:], p[1:]) for i in range(len(s), -1, -1))
            if p[0] == '?':
                return is_match(s[1:], p[1:])
            return s[0] == p[0] and is_match(s[1:], p[1:])

        while '**' in p:
            p = p.replace('**', '*')
        return is_match(s, p)


s = Solution()
assert not s.isMatch(s="aa", p="a")
assert s.isMatch(s="aa", p="*")
assert not s.isMatch(s="cb", p="?a")
assert s.isMatch(s="adceb", p="a*b")
assert not s.isMatch(s="acdcb", p="a*c?b")
assert not s.isMatch(
    s="aabbbabaaaaaabbabbaabbabbbabaabaaabbbabbabbbbababbabaaaaaabaabaabbbababaaabbaabaaabaabaabaaabaaababbaabababbabbababbbbabbababbbababaaaabaabbbabababaabbbaaababbbbbbbbabaaabbaabbbaababaaaababababbabbbbbb",
    p="a*bab***b**abbabaa**a*a**b****b*b*****b*bb***a**a**a***baba*abbbaa***bb**bbabb*b*b*bab*a****a*bb*a**b")
