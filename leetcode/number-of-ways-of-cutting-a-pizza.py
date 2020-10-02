from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        _MODER = 10 ** 9 + 7
        if not pizza:
            return 0

        n, m = len(pizza), len(pizza[0])
        pizza = ['.' * (m + 2)] + ['.' + _ + '.' for _ in pizza] + ['.' * (m + 2)]

        rest = [[0] * (m + 2) for _ in range(n + 2)]
        for i in range(n, -1, -1):
            acc_row_sum = 0
            for j in range(m, -1, -1):
                if pizza[i][j] == 'A':
                    acc_row_sum += 1
                rest[i][j] = rest[i + 1][j] + acc_row_sum

        t = [[[0] * k for _ in range(m + 2)] for _ in range(n + 2)]
        t[0][0][0] = 1

        for i in range(0, n + 1):
            for j in range(0, m + 1):
                for l in range(1, k):
                    if rest[i + 1][j + 1] < k - l:
                        continue
                    for a in range(i):
                        if rest[i + 1][j + 1] == rest[a + 1][j + 1]:
                            continue
                        t[i][j][l] += t[a][j][l - 1]
                    for b in range(j):
                        if rest[i + 1][j + 1] == rest[i + 1][b + 1]:
                            continue
                        t[i][j][l] += t[i][b][l - 1]
                    t[i][j][l] %= _MODER

        total_cuts = 0
        for i in range(n + 1):
            for j in range(m + 1):
                total_cuts = (total_cuts + t[i][j][k - 1]) % _MODER
        return total_cuts


s = Solution()

assert s.ways(pizza=["A..", "AAA", "..."], k=3) == 3
assert s.ways(pizza=[".A", "AA", "A."], k=3) == 3
assert s.ways(pizza=["A..", "AA.", "..."], k=3) == 1
assert s.ways(pizza=["A..", "A..", "..."], k=1) == 1
