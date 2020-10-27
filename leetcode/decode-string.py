from string import digits


class Solution:
    def decodeString(self, s: str) -> str:
        v, t = 0, ''
        num_stack, tok_stack = [], []
        for e in s:
            if e in digits:
                v = v * 10 + int(e)
            elif e == '[':
                num_stack.append(v)
                tok_stack.append(t)
                v, t = 0, ''
            elif e == ']':
                t = tok_stack.pop() + t * num_stack.pop()
            else:
                t += e
        return t


s = Solution()
assert s.decodeString(s="3[a]2[bc]") == "aaabcbc"
assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
assert s.decodeString("abc3[cd]xyz") == "abccdcdcdxyz"
