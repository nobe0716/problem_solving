di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

m, n = int(raw_input()), int(raw_input())
g = ['1' * (n + 2) for x in range(m + 2)]
v = list()
v = [[True for x in range(n + 2)]] + [[True] + [False for x in range(n)] + [True] for x in range(m)] + [[True for x in range(n + 2)]]

for i in range(1, m + 1):
    g[i] = ['1'] + raw_input().split() + ['1']


def search(g, v, i, j):
    if v[i][j] or g[i][j] == '0':
        return 0
    v[i][j] = True
    return sum([search(g, v, i + di[x], j + dj[x]) for x in range(8)]) + 1

l = 0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if g[i][j] == '1' and not v[i][j]:
            l = max([l, search(g, v, i, j)])
print(l)