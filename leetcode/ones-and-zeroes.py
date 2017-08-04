class Solution(object):
    def findMaxForm(self, strs, m, n):
        t = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                row.append(0)
            t.append(row)

        for s in strs:
            zeroes = 0
            ones = 0
            for c in s:
                if c == '0':
                    zeroes += 1
                else:
                    ones += 1
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    if t[i][j] < t[i - zeroes][j - ones] + 1:
                        t[i][j] = t[i - zeroes][j - ones] + 1
        return t[m][n]

s = Solution()
assert s.findMaxForm(["10","0001","111001","1","0"], 5, 3) is 4
assert s.findMaxForm(["10","0001","111001","1","0"], 3, 4) is 3
assert s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) is 4
assert s.findMaxForm(["10", "0", "1"], 1, 1) is 2
