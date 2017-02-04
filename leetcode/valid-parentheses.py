class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c == ')' and stack.pop(-1) != '(':
                return False
            elif c == '}' and stack.pop(-1) != '{':
                return False
            elif c == ']' and stack.pop(-1) != '[':
                return False
        return True

s = Solution()
assert(s.isValid("()") == True)
assert(s.isValid("(}") == False)
assert(s.isValid("{[()]{}}") == True)