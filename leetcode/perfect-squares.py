class Solution(object):
    def numSquares(self, n):
        if n == 0:
            return 0
        t = [i for i in range(n + 1)]
        s = []
        i = 1
        while i * i <= n:
            t[i * i] = 1
            s.append(i * i)
            i += 1
        # s consist of square values between [1, n]

        q = list(s)
        while len(q) > 0:
            nq = []

            for i in q:
                for j in s:
                    if i + j > n:
                        continue
                    if t[i + j] > t[i] + t[j]:
                        t[i + j] = t[i] + t[j]
                        nq.append(i + j)
            q = nq
        return t[n]


s = Solution()
print(s.numSquares(2))
print(s.numSquares(12))
print(s.numSquares(13))
print(s.numSquares(10000))
print(s.numSquares(100000))