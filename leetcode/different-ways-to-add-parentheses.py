import itertools
from string import digits
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # tokenize
        digit_token = None
        tokens = []

        for ch in expression:
            if ch in digits:
                if digit_token:
                    digit_token += ch
                else:
                    digit_token = ch
            else:
                if digit_token:
                    tokens.append(digit_token)
                    digit_token = None
                tokens.append(ch)
        if digit_token:
            tokens.append(digit_token)

        def rec(equation: List[str]) -> List[int]:  # parenthesis starts on i
            if len(equation) == 1:
                return [int(equation[0])]

            res = []
            for i in range(1, len(equation), 2):
                lo = rec(equation[:i])
                ro = rec(equation[i + 1:])
                op = equation[i]
                for lv, rv in itertools.product(lo, ro):
                    res.append(eval('{}{}{}'.format(lv, op, rv)))
            return res

        ans = sorted(rec(tokens))
        # print(ans)
        return ans


s = Solution()
# assert s.diffWaysToCompute('2-1-1') == [0, 2]
assert s.diffWaysToCompute("2*3-4*5") == [-34, -14, -10, -10, 10]
