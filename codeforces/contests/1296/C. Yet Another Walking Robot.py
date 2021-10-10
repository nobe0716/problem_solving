# https://codeforces.com/problemset/problem/1296/C
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, s):
    x = y = 0
    dx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    dy = {'L': 0, 'R': 0, 'U': -1, 'D': 1}

    visited = {(0, 0): 0}
    LIMIT = 2 * 10 ** 5 + 2
    ans = (0, LIMIT)
    for i, e in enumerate(s, start=1):
        x, y = x + dx[e], y + dy[e]
        if (x, y) in visited:
            if i - visited[(x, y)] + 1 < ans[1] - ans[0] + 1:
                ans = visited[(x, y)] + 1, i
        visited[(x, y)] = i

    return ans if ans[1] != LIMIT else [-1]


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    ans = solve(n, s)
    print(' '.join(map(str, ans)))
