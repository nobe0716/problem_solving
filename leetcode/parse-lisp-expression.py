import sys
from collections import defaultdict

sys.setrecursionlimit(1000)


class Solution:
    def evaluate(self, expression: str) -> int:
        def solve(exp, i, var_stack):
            if exp[i] != '(':
                var = exp[i:].split(' ', 1)[0]
                var_name = var
                while var_name[-1] == ')':
                    var_name = var_name[:-1]

                if var_name not in var_stack:
                    return int(var_name), len(var)
                else:
                    return var_stack[var_name][-1], len(var)
            else:
                if exp[i:i + 4] == '(add':
                    i += len('(add ')
                    va, la = solve(exp, i, var_stack)
                    vb, lb = solve(exp, i + la + 1, var_stack)
                    return va + vb, la + lb + 6
                elif exp[i:i + 5] == '(mult':
                    i += len('(mult ')
                    va, la = solve(exp, i, var_stack)
                    vb, lb = solve(exp, i + la + 1, var_stack)
                    return va * vb, la + lb + 7
                else:  # let
                    j = i
                    j += len('(let ')

                    var_names = []
                    while not (exp[j] in '0123456789(' or exp[j:].split(' ', 1)[0].endswith(')')):
                        var_name = exp[j:].split(' ', 1)[0]
                        j += len(var_name) + 1
                        var_names.append(var_name)

                        var_value, var_exp_len = solve(exp, j, var_stack)

                        var_stack[var_name].append(var_value)
                        j += var_exp_len + 1

                    expr, expr_len = solve(exp, j, var_stack)

                    for var_name in var_names:
                        var_stack[var_name].pop()

                    j += expr_len
                    return expr, j - i

        # (let a1 3 b2 (add a1 1) b2)

        res = solve(expression, 0, defaultdict(list))
        return res[0]


s = Solution()
assert s.evaluate('(let x 2 (mult x (let x 3 y 4 (add x y))))') == 14
assert s.evaluate('(add 1 2)') == 3
assert s.evaluate('(mult 3 (add 2 3))') == 15
assert s.evaluate('(let x 3 x 2 x)') == 2
assert s.evaluate('(let x 1 y 2 x (add x y) (add x y))') == 5
assert s.evaluate('(let x 2 (add (let x 3 (let x 4 x)) x))') == 6
assert s.evaluate('(let a1 3 b2 (add a1 1) b2)') == 4
