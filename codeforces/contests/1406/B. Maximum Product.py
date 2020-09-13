import sys

input = sys.stdin.readline


def solve(n, a):
    a = [0] + a
    min_table = [[float('inf')] * (n + 1) for _ in range(6)]
    max_table = [[float('-inf')] * (n + 1) for _ in range(6)]

    # min_table[1][0] =
    # max_table[1][0] = float
    for j in range(1, n + 1):
        min_table[1][j] = min(a[j], min_table[1][j - 1])
        max_table[1][j] = max(a[j], max_table[1][j - 1])
    for i in range(2, 6):
        for j in range(i, n + 1):
            if a[j] > 0:
                min_table[i][j] = min(a[j] * min_table[i - 1][j - 1], min_table[i][j - 1])
                max_table[i][j] = max(a[j] * max_table[i - 1][j - 1], max_table[i][j - 1])
            else:  # a[j] < 0
                min_table[i][j] = min(a[j] * max_table[i - 1][j - 1], min_table[i][j - 1])
                max_table[i][j] = max(a[j] * min_table[i - 1][j - 1], max_table[i][j - 1])
    return max_table[5][n]


# assert solve(5, list(map(int, '-1 -2 -3 -4 -5'.split()))) == -120
# assert solve(6, list(map(int, '-1 -2 -3 1 2 -1'.split()))) == 12
# assert solve(6, list(map(int, '-1 0 0 0 -1 -1'.split()))) == 0
# assert solve(6, list(map(int, '-9 -7 -5 -3 -2 1'.split()))) == 945

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    v = solve(n, a)
    print(v)
