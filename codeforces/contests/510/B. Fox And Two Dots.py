# https://codeforces.com/problemset/problem/510/B
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline

sys.setrecursionlimit(3000)


def solve(n, m, g):
    def is_valid_pos(x, y):
        return 0 <= x < n and 0 <= y < m

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def dfs(x, y):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not is_valid_pos(nx, ny):
                continue
            if g[nx][ny] == g[x][y]:
                if v[nx][ny] == 0:
                    v[nx][ny] = v[x][y] + 1
                    if dfs(nx, ny):
                        return True
                else:
                    if v[x][y] - v[nx][ny] >= 3:
                        return True
        return False

    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if v[i][j] == 0:
                v[i][j] = 1
                if dfs(i, j):
                    return True
    return False


n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]
ans = solve(n, m, g)
print('Yes' if ans else 'No')
