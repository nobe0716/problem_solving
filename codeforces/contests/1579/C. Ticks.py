# 2022-09-17 17:11:38.379467
# https://codeforces.com/problemset/problem/1579/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, m, k, g):
    verified = [[None] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m - 1):
            if g[i][j] != '*':
                continue
            x = 1
            while 0 <= i - x and 0 <= j - x and j + x < m and g[i - x][j - x] == '*' and g[i - x][j + x] == '*':
                x += 1
            x -= 1
            if x < k:
                continue
            # print('fill {},{} to {}'.format(i, j, x))
            while x > 0:
                verified[i - x][j - x] = verified[i - x][j + x] = True
                x -= 1
            verified[i][j] = True
    for i in range(n):
        for j in range(m):
            if g[i][j] == '*' and not verified[i][j]:
                return False
    return True


assert proc(4, 9, 2, ['*.*.*...*', '.*.*...*.', '..*.*.*..', '.....*...'])

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    g = []
    for _ in range(n):
        g.append(input().strip())

    ans = proc(n, m, k, g)
    print('YES' if ans else 'NO')
