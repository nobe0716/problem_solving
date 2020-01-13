class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        i = 1
        r = 0
        while i <= max(a, b, c):
            if i & c > 0 and i & a == 0 and i & b == 0:
                r += 1
            elif i & c == 0:
                if i & a > 0:
                    r += 1
                if i & b > 0:
                    r += 1
            i *= 2
        return r


s = Solution()
assert s.minFlips(2, 6, 5) == 3
assert s.minFlips(4, 2, 7) == 1
assert s.minFlips(1, 2, 3) == 0
assert s.minFlips(5, 2, 8) == 4
