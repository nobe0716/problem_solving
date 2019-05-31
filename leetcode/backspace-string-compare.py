class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def proc(v: str) -> str:
            stack = []
            for e in v:
                if e == '#':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(e)
            return ''.join(stack)

        return proc(S) == proc(T)
