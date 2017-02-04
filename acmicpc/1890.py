n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * n for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        if m[i][j] == 0:
            continue
        if i + m[i][j] < n:
            d[i + m[i][j]][j] += d[i][j]
        if j + m[i][j] < n:
            d[i][j + m[i][j]] += d[i][j]
print(d[n - 1][n - 1])
