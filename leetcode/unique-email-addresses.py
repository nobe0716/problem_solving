"""
## Name of Prob
Unique Email Addresses

## Link
https://leetcode.com/problems/unique-email-addresses/

## Note

## Input
list of emails

len(list) <= 100
each len(email) <= 100


## Output

## Strategy
normalize each given email and add it to set
return size of set

normalize using regex ([^+]+).*@(.*)
second group will be domain name
if we replace all '.' of first group, it will be id

id@domain will be normalized url

"""
import re
from typing import List

_DEBUG = True


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        REGEX = r'([^+]+).*@(.*)'
        p = re.compile(REGEX)

        def normalize_url(email: str) -> str:
            m = p.match(email)
            return m.group(1).replace('.', '') + '@' + m.group(2)

        return len(set(map(normalize_url, emails)))


s = Solution()
assert s.numUniqueEmails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]) == 2
