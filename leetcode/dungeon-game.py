from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])

        def validate(initial_hp: int) -> bool:
            t = [[0 for _ in range(m)] for _ in range(n)]
            v = [[True for _ in range(m)] for _ in range(n)]
            t[0][0] = initial_hp
            for i in range(n):
                for j in range(m):
                    d = dungeon[i][j]
                    if i == 0 and j == 0:
                        t[i][j] += d
                    elif j == 0:
                        t[i][j] = t[i - 1][j] + d if v[i - 1][j] else 0
                    elif i == 0:
                        t[i][j] = t[i][j - 1] + d if v[i][j - 1] else 0
                    else:
                        t[i][j] = t[i - 1][j] + d if v[i - 1][j] else 0
                        t[i][j] = max(t[i][j], t[i][j - 1] + d if v[i][j - 1] else 0)
                    if t[i][j] <= 0:
                        t[i][j] = 0
                        v[i][j] = False
            return v[n - 1][m - 1]

        hi = 2
        while not validate(hi):
            hi *= 2

        lo = hi // 2
        res = hi
        while lo <= hi:
            p = (lo + hi) // 2
            if validate(p):
                res = min(res, p)
                hi = p - 1
            else:
                lo = p + 1
        return res


s = Solution()
assert s.calculateMinimumHP(dungeon=[
    [1, -3, 3],
    [0, -2, 0],
    [-3, -3, -3]]) == 3
assert s.calculateMinimumHP(dungeon=[[3, -20, 30], [-3, 4, 0]]) == 1
assert s.calculateMinimumHP(dungeon=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7
assert s.calculateMinimumHP(dungeon=[[0]]) == 1
assert s.calculateMinimumHP(dungeon=[[100]]) == 1
