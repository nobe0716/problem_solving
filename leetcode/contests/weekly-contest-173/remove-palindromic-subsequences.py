class Solution:
    def removePalindromeSub(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0
        if l == 1 or s == s[::-1]:
            return 1
        return 2


s = Solution()
# assert s.removePalindromeSub('ababa') == 1
assert s.removePalindromeSub('abb') == 2
# assert s.removePalindromeSub('baabb') == 2
