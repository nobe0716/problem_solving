# https://codeforces.com/problemset/problem/1366/C
import sys
from collections import Counter, defaultdict

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n: int, m: int, grid) -> int:
    d = defaultdict(lambda: Counter())
    s = defaultdict(int)
    for i in range(n):
        for j in range(m):
            if (n + m) % 2 == 0 and (i + j) == (m + n - 1) // 2:
                continue
            k = min(i + j, m + n - i - j - 2)
            d[k][grid[i][j]] += 1
            s[k] += 1

    # print(d)
    ans = 0
    for k, c in d.items():
        v = c.most_common(1)[0][1]
        ans += (s[k] - v)
    return ans


for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [[int(x) for x in input().strip().split()] for _ in range(n)]
    print(solve(n, m, grid))
