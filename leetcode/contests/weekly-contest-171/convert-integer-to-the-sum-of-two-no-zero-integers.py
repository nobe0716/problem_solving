from string import ascii_lowercase


class Solution:
    def freqAlphabets(self, s: str) -> str:
        l = len(s)
        d = ' ' + ascii_lowercase
        r = ''

        i = 0
        while i < l:
            if i + 2 < l and s[i + 2] == '#':
                r += d[int(s[i:i + 2])]
                i += 3
            else:
                r += d[int(s[i])]
                i += 1
        return r


s = Solution()
assert 'jkab' == s.freqAlphabets('10#11#12')
assert 'acz' == s.freqAlphabets('1326#')
assert 'abcdefghijklmnopqrstuvwxyz' == s.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")
