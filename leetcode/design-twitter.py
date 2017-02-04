import re

class Solution(object):
    def validUtf8(self, data):
        p = r"^(0[01]{7}|110[01]{5}10[01]{6}|1110[01]{4}10[01]{6}10[01]{6}|11110[01]{3}10[01]{6}10[01]{6}10[01]{6})*$"
        bs = "".join(map(lambda x: format(x, "08b"), data))
        print(bs)
        return re.match(p, bs) != None

s = Solution()
print(s.validUtf8([235, 140, 4]))
print(s.validUtf8([197, 130, 1]))
print(s.validUtf8([230,136,145]))

