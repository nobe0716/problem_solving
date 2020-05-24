_MODULO = 10 ** 8


def solve(n1, n2, k1, k2):
    t = [[[[0 for _ in range(k2 + 1)] for _ in range(k1 + 1)] for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    #
    t[0][0][0][0] = 1
    t[1][0][1][0] = 1
    t[0][1][0][1] = 1
    # for i in range(1, min(k1, n1)):
    #     t[i][0][i][0] = 1
    # for i in range(1, min(k2, n2)):
    #     t[0][i][0][i] = 1

    for i in range(0, n1 + 1):
        for j in range(0, n2 + 1):
            if i == 0 and j == 0:
                continue

            if i > 0:
                for k in range(1, k2 + 1):
                    t[i][j][1][0] += t[i - 1][j][0][k]
                for k in range(2, k1 + 1):
                    t[i][j][k][0] += t[i - 1][j][k - 1][0]

            if j > 0:
                for k in range(1, k1 + 1):
                    t[i][j][0][1] += t[i][j - 1][k][0]
                for k in range(2, k2 + 1):
                    t[i][j][0][k] += t[i][j - 1][0][k - 1]

    r = 0
    for k in range(1, k1 + 1):
        r = (r + t[n1][n2][k][0]) % _MODULO

    for l in range(1, k2 + 1):
        r = (r + t[n1][n2][0][l]) % _MODULO
    # print(n1, n2, k1, k2, r)
    return r


# assert solve(2, 1, 1, 10) == 1
# assert solve(2, 3, 1, 2) == 5
# assert solve(2, 4, 1, 1) == 0
# assert solve(100, 100, 10, 10) == 950492
n1, n2, k1, k2 = map(int, input().split())

# n1, n2, k1, k2 = 100, 100, 10, 10
# n1, n2, k1, k2 = 2, 1, 1, 1

print(solve(n1, n2, k1, k2))
