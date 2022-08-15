# 2022-08-15T22:19:47Z
import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m, k = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(input().strip())

query = []
for _ in range(k):
    x, y = map(int, input().split())
    query.append((x, y))

group = [[0] * m for _ in range(n)]
color = [[[0] * 4 for _ in range(m)] for _ in range(n)]
group_to_picture = [0]


def unavailable(x, y):
    return group[x][y] > 0 or grid[x][y] == '*'


group_no = 0
for i in range(1, n):
    for j in range(1, m):
        if unavailable(i, j):
            continue

        s = [(i, j)]

        group_no += 1
        picture_count = 0

        group[i][j] = group_no
        while s:
            x, y = s.pop()
            for d, xy in enumerate([(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]):
                nx, ny = xy
                if unavailable(nx, ny):
                    if grid[nx][ny] == '*' and color[nx][ny][d] != group_no:
                        color[nx][ny][d] = group_no
                        picture_count += 1

                    continue
                group[nx][ny] = group_no
                s.append((nx, ny))

        group_to_picture.append(picture_count)

for x, y in query:
    print('{}\n'.format(group_to_picture[group[x - 1][y - 1]]))
