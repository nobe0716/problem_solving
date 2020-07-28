for _ in range(int(input())):
    n, k = map(int, input().split())
    grid = [[0] * n for _ in range(n)]
    x = y = 0
    for _ in range(k):
        grid[x][y] = 1
        y += 1
        x += 1
        if y >= n:
            y = 0
            x += 1
        x, y = x % n, y % n
    print(2 if k % n else 0)
    print('\n'.join(''.join(map(str, e)) for e in grid))
