class Solution(object):
    def __init__(self):
        self.t = []

    def dp(self, a, b):
        if self.t[a][b] is not None:
            return self.t[a][b]
        min_cost = 999999999999999999
        for i in range(a + 1, b):
            cost = i + max([self.dp(a, i - 1) , self.dp(i + 1, b)])
            min_cost = min([cost, min_cost])
        self.t[a][b] = min_cost
        return min_cost

    def getMoneyAmount(self, n):
        self.t = [[None for x in range(n + 1)] for y in range(n + 1)]
        for i in range(n + 1):
            self.t[i][i] = 0
            if i > 0:
                self.t[i - 1][i] = i - 1
            if i > 1:
                self.t[i - 2][i] = i - 1
        return self.dp(1, n)

l = []
l2 = []
l.append(l2)
s = Solution()
print(s.getMoneyAmount(7))

assert(s.getMoneyAmount(1) == 0)
assert(s.getMoneyAmount(2) == 1)
assert(s.getMoneyAmount(3) == 2)
assert(s.getMoneyAmount(4) == 4)
assert(s.getMoneyAmount(7) == 10)