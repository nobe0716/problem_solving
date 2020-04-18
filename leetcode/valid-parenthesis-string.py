class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        lb = rb = 0
        for i, e in enumerate(s):
            if e in '(*':
                lb += 1
            else:
                lb -= 1

            if s[n - i - 1] in '*)':
                rb += 1
            else:
                rb -= 1

            if lb < 0 or rb < 0:
                return False
        return True

