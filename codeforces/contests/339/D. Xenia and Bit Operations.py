n, m = map(int, input().split())

a = [[0] + list(map(int, input().split()))]

k = 2 ** (n - 1)
for i in range(1, n + 1):
    row = [0]
    for j in range(1, k + 1):
        if i % 2 == 1:
            row.append(a[i - 1][j * 2 - 1] | a[i - 1][j * 2])
        else:
            row.append(a[i - 1][j * 2 - 1] ^ a[i - 1][j * 2])
    a.append(row)
    k //= 2

pbs = [map(int, input().split()) for _ in range(m)]
r = []
for p, b in pbs:
    if a[0][p] != b:
        a[0][p] = b
        for i in range(0, n):
            j = p + (1 if p % 2 == 1 else -1)
            if i % 2 == 0:
                b = a[i][j] | b
            else:
                b = a[i][j] ^ b
            p = (p + 1) // 2
            if a[i + 1][p] == b:
                break
            a[i + 1][p] = b
    r.append(a[n][1])

print('\n'.join(map(str, r)))
