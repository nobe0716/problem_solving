from string import digits


class Solution:
    def calculate(self, s: str) -> int:
        digit_set = set(digits)

        equations = []
        stack = []

        s = s.replace(' ', '').strip()

        dg_buf = 0
        num_start = False
        for e in s:
            if e in digit_set:
                num_start = True
                dg_buf = dg_buf * 10 + int(e)
                continue

            if num_start:
                equations.append(dg_buf)
                dg_buf = 0
                num_start = False

            if e == '+' or e == '-':
                while stack and stack[-1] != '(':
                    equations.append(stack.pop())
                stack.append(e)
            elif e == '(':
                stack.append('(')
            elif e == ')':
                while stack and stack[-1] != '(':
                    equations.append(stack.pop())
                stack.pop()

        if s[-1] not in '+-()':
            equations.append(dg_buf)

        while stack:
            equations.append(stack.pop())

        for e in equations:
            if type(e) is int:
                stack.append(e)
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(a + b if e == '+' else a - b)

        return stack[-1]


s = Solution()
assert s.calculate("0") == 0
assert s.calculate("1 + 0 - 2") == -1
assert s.calculate("(1+(4+5+2)-3)+(6+8)") == 23
assert s.calculate(" 2-1 + 2 ") == 3
assert s.calculate("1 + 1") == 2
assert s.calculate(" 2-1 + 2 ") == 3
