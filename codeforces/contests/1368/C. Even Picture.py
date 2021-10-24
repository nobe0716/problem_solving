# https://codeforces.com/problemset/problem/1368/C
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline

n = int(input())
g = [[0] * (1 + (n + 1) * 2) for _ in range(5)]

for i in range(n + 1):
    x = i * 2
    g[2][x] = g[2][x + 1] = g[2][x + 2] = 1

    if i % 2 == 0:
        g[1][x] = g[0][x] = g[0][x + 1] = g[0][x + 2] = g[1][x + 2] = 1
    else:
        g[3][x] = g[4][x] = g[4][x + 1] = g[4][x + 2] = g[3][x + 2] = 1

k = sum(sum(g[x]) for x in range(5))
print(k)
for i in range(5):
    for j in range(len(g[0])):
        if g[i][j] == 1:
            print(i, j)
