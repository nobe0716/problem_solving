from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(' ')
        row = max(map(len, s))
        col = len(s)
        print(row)
        t = [[' '] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                e = s[j]
                if i < len(e):
                    t[i][j] = e[i]
        return [''.join(x).rstrip() for x in t]


s = Solution()
print(s.printVertically("TO BE OR NOT TO BE"))

print(["TBONTB", "OEROOE", "   T"])
