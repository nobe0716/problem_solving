class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        idx = s.find('6')
        s = list(s)
        s[idx] = '9'
        return int(''.join(s))


s = Solution()
print(s.maximum69Number(6666))
