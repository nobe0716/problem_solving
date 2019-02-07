n = int(input())
m = [input() for _ in range(n)]
c = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if m[i][j] == 'X' and m[i - 1][j - 1] == 'X' and m[i - 1][j + 1] == 'X' and m[i + 1][j - 1] == 'X' and m[i + 1][
            j + 1] == 'X':
            c += 1
print(c)
