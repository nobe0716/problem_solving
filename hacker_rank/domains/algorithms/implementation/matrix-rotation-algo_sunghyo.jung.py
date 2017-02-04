__author__ = 'sunghyo.jung'

def shift(matrix, m, n, level, rotation):
    for r in xrange(rotation):
        v = matrix[level][level]
        for i in range(level, level + n - 1):
            matrix[level][i] = matrix[level][i + 1]
        for i in range(level, level + m - 1):
            matrix[i][n + level - 1] = matrix[i + 1][n + level - 1]
        for i in range(n + level - 1, level, -1):
            matrix[m + level - 1][i] = matrix[m + level - 1][i - 1]
        for i in range(m + level - 1, level, -1):
            matrix[i][level] = matrix[i - 1][level]
        matrix[level + 1][level] = v
    return matrix

m, n, r = map(int, raw_input().split())
matrix = []
for i in xrange(m):
    matrix.append(map(int, raw_input().split()))

var_m, var_n = m, n
for i in range(min(m, n) / 2):
    real_r = r % ((var_m + var_n) * 2 - 4)
    matrix = shift(matrix, var_m, var_n, i, real_r)
    var_m, var_n = var_m - 2, var_n - 2

for i in xrange(m):
    for j in xrange(n):
        print matrix[i][j],
    print ''