import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a == b or b in a:
            return 1
        if len(a) < len(b):
            cnt = int(math.ceil(len(b) / len(a)))
            na = a * cnt
            if b in na:
                return cnt
            cnt += 1
            na += a
            if b in na:
                return cnt

            return -1
        a = a * 2
        if b in a:
            return 2
        return -1


s = Solution()
assert s.repeatedStringMatch(a="abcd", b="cdabcdab") == 3
assert s.repeatedStringMatch(a="a", b="aa") == 2
assert s.repeatedStringMatch(a="a", b="a") == 1
assert s.repeatedStringMatch(a="abc", b="wxyz") == -1
