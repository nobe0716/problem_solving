n, m = map(int, input().split())
g = ['.' * (m + 1)]
for _ in range(n):
    g.append('.' + input())

t = [[0 for i in range(m + 1)] for j in range(n + 1)]
t[0][1] = 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if g[i][j] == '.':
            t[i][j] = t[i - 1][j] + t[i][j - 1]
print(t[n][m])

for i in range(1, n + 1):
    print(t[i][1:])
