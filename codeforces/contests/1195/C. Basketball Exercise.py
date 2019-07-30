n = int(input())
p = [[0] * (n + 1)] + [([0] + list(map(int, input().split()))) for _ in range(2)]
t = [[0] * (n + 1) for _ in range(3)]
t[1][1], t[2][1] = p[1][1], p[2][1]

for i in range(2, n + 1):
    t[0][i] = max(t[1][i - 1], t[2][i - 1])
    t[1][i] = p[1][i] + max(t[0][i - 1], t[2][i - 1])
    t[2][i] = p[2][i] + max(t[0][i - 1], t[1][i - 1])
print(max(t[0][n], t[1][n], t[2][n]))
