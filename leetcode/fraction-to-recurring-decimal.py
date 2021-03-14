class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        s = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        w, r = divmod(numerator, denominator)
        s += '{}.'.format(str(w))
        d = {r: len(s)}
        while r > 0:
            w, r = divmod(r * 10, denominator)
            s += str(w)

            if r in d:
                return '{}({})'.format(s[:d[r]], s[d[r]:])
            d[r] = len(s)

        return s


s = Solution()
assert s.fractionToDecimal(1, 2) == '0.5'
assert s.fractionToDecimal(1, 3) == '0.(3)'
assert s.fractionToDecimal(-50, 8) == '-6.25'
print(s.fractionToDecimal(1, 7))
