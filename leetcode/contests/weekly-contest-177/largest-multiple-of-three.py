from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        d = {0: [], 1: [], 2: []}
        sum_of_mod = 0
        digits = sorted(digits, reverse=True)
        for e in digits:
            d[e % 3].append(e)
            sum_of_mod += (e % 3)

        if sum_of_mod % 3 == 1:
            if len(d[1]) > 0:
                digits.remove(d[1].pop())
            elif len(d[2]) >= 2:
                digits.remove(d[2].pop())
                digits.remove(d[2].pop())
            else:
                return ""
        elif sum_of_mod % 3 == 2:
            if len(d[2]) > 0:
                digits.remove(d[2].pop())
            elif len(d[1]) >= 2:
                digits.remove(d[1].pop())
                digits.remove(d[1].pop())
            else:
                return ""

        if len(digits) == 0:
            return ""
        joined_str = ''.join(map(str, digits))
        return joined_str if joined_str[0] != '0' else "0"


s = Solution()
assert s.largestMultipleOfThree([9, 8, 6, 8, 6]) == "966"
assert s.largestMultipleOfThree([8, 1, 9]) == "981"
assert s.largestMultipleOfThree([8, 6, 7, 1, 0]) == "8760"
assert s.largestMultipleOfThree([1]) == ""
assert s.largestMultipleOfThree([0, 0, 0, 0, 0, 0]) == "0"
