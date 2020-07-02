dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solve(n, m, maze):
    total_good_count = 0

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if maze[x][y] == 'B':
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if maze[nx][ny] == 'G':
                        return False
                    elif maze[nx][ny] == '.':
                        maze[nx][ny] = '#'
            elif maze[x][y] == 'G':
                total_good_count += 1

    visited = [[False] * (m + 2) for _ in range(n + 1)]
    stack = [(n, m)] if maze[n][m] == '.' else []
    visited[n][m] = True
    escapable_good_count = 0
    while stack:
        x, y = stack.pop()
        if maze[x][y] == 'G':
            escapable_good_count += 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (maze[nx][ny] == '.' or maze[nx][ny] == 'G') and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))

    return escapable_good_count == total_good_count


for _ in range(int(input())):
    n, m = map(int, input().split())
    maze = [['#'] * (m + 2)]
    for _ in range(n):
        row = input()
        maze.append(['#'] + list(row) + ['#'])
    maze.append(['#'] * (m + 2))

    r = solve(n, m, maze)
    print('Yes' if r else 'No')
