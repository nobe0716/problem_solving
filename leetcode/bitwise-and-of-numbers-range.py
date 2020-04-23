class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        base = 1
        r = ''
        while base <= m or base <= n:
            if n & base and m & base and n // base == m // base:
                r += '1'
            else:
                r += '0'
            base *= 2
        r += '0'
        return int(r[::-1], 2)
