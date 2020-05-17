"""
Tough bfs
"""
import sys

sys.setrecursionlimit(327500)
# sys.stdin = open('a.large')

n, m, k = map(int, input().split())
maze = [list(input()) for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]


def is_visitable(x, y):
    if not (0 <= x < n and 0 <= y < m):
        return False
    return maze[x][y] == '.' and not visited[x][y]


open_count = 0
for i in range(n):
    for j in range(m):
        if maze[i][j] == '.':
            open_count += 1

visited_count = 0
for i in range(n):
    for j in range(m):
        if maze[i][j] != '.' or visited[i][j]:
            continue
        if open_count - visited_count == k:
            break

        visited_count += 1
        visited[i][j] = True
        stack = [(i, j)]

        while stack and open_count - visited_count > k:
            x, y = stack.pop()
            if open_count - visited_count == k:
                break

            for d in range(4):
                if open_count - visited_count == k:
                    break
                nx = x + di[d]
                ny = y + dj[d]
                if not is_visitable(nx, ny):
                    continue
                visited_count += 1
                visited[nx][ny] = True
                stack.append((nx, ny))

for i in range(n):
    for j in range(m):
        if maze[i][j] == '.' and not visited[i][j]:
            maze[i][j] = 'X'

for _ in range(n):
    print(''.join(maze[_]))
