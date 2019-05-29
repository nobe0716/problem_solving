"""
## Name of Prob
482. License Key Formatting

## Link
https://leetcode.com/problems/license-key-formatting/

## Note
consists only alphanumeric character and dashes.


## Input
one str

## Output
re formatted str

## Strategy
remove dash from given str and upper
divide given str from back with exactly K size
return joined group by dash

"""


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        upppered_s = S.replace('-', '').upper()
        len_s = len(upppered_s)
        groups = []
        pos = len_s % K
        if pos > 0:
            groups.append(upppered_s[:pos])

        for i in range(len_s // K):
            groups.append(upppered_s[pos:pos + K])
            pos += K
        return '-'.join(groups)


s = Solution()
assert s.licenseKeyFormatting(S="5F3Z-2e-9-w", K=4) == "5F3Z-2E9W"
assert s.licenseKeyFormatting(S="A5F3Z-2e-9-w", K=4) == "A-5F3Z-2E9W"
