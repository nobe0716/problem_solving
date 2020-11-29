class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = ' ' + word1
        word2 = ' ' + word2
        n, m = len(word1), len(word2)

        """
        T(i, j) : min # of ops if match word1[i] to word2[j]
        T(i, j) = T(k, l) + (i - k - 1; deleted chr) + (j - l - 1 ; inserted chr)
        """
        t = [[float('inf') for _ in range(m)] for _ in range(n)]
        r = [[float('inf') for _ in range(m)] for _ in range(n)]

        t[0][0] = 0
        # cache min among t[:k][:l] - k - 1 - l - 1
        r[0][0] = -2

        for i in range(1, n):
            t[i][0] = i  # cus i number of chr should be deleted
            r[i][0] = -2

        for i in range(1, m):
            t[0][i] = i  # cus i number of chr should be inserted
            r[0][i] = -2

        for i in range(1, n):
            for j in range(1, m):
                t[i][j] = r[i - 1][j - 1] + i + j
                if word1[i] != word2[j]:
                    t[i][j] += 1

                r[i][j] = min(t[i][j] - i - 1 - j - 1, r[i - 1][j], r[i][j - 1])

        res = float('inf')
        for i in range(n):
            for j in range(m):
                res = min(res, t[i][j] + (n - i - 1) + (m - j - 1))
        return res


s = Solution()
assert s.minDistance("", "") == 0
assert s.minDistance("horse", "ros") == 3
assert s.minDistance("intention", "execution") == 5
assert s.minDistance(
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef",
    "bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg") == 2
