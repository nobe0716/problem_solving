from collections import defaultdict
from sys import stdin

n, m = map(int, input().split())

g = ['.' * (m + 1)]
for _ in range(n):
    g.append('.' + stdin.readline())


def solve(n, m, g):
    t = [[0] * (m + 2) for j in range(n + 2)]
    t[0][1] = 1
    t[n + 1][m] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if g[i][j] == '#':
                t[i][j] = 0
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    if t[n][m] == 0: # not rechable
        return 0
    d = defaultdict(int)
    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            if t[i][j] == 0:
                continue
            else:
                t[i][j] = max(t[i + 1][j], t[i][j + 1])

            if t[i][j] == 1:
                v = i - 1 + j - 1
                d[v] += 1

    return min(d[x] for x in range(1, n + m - 2))


r = solve(n, m, g)
print(r)
