def solve(n, m, g):
    def valid(x, y):
        return 0 <= x < n and 0 <= y < m and g[x][y] == 1 and c[x][y] == -1

    def traverse(x, y):
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if valid(nx, ny):
                yield nx, ny

    q = [(0, 0)]
    c = [[-1] * m for _ in range(n)]

    c[0][0] = 1
    while q and c[n - 1][m - 1] == -1:
        nq = set()
        for x, y in q:
            for nx, ny in traverse(x, y):
                c[nx][ny] = c[x][y] + 1
                nq.add((nx, ny))
        q = nq
    return c[n - 1][m - 1]


n, m = map(int, input().split())
g = [[int(x) for x in list(input())] for _ in range(n)]

print(solve(n, m, g))
