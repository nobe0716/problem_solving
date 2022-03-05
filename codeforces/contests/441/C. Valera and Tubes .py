# 2022-03-05 17:15:17.986835
# https://codeforces.com/problemset/problem/441/C
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write

n, m, k = map(int, input().split())


def proc(n, m, k):
    t = [[False] * (m + 2) for _ in range(n + 2)]
    for i in range(n + 2):
        t[i][0] = t[i][m + 1] = True
    for i in range(m + 2):
        t[0][i] = t[n + 1][i] = True

    next_x = next_y = 1
    t[next_x][next_y] = True
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    stack = [(next_x, next_y)]
    path = [(next_x, next_y)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if t[next_x][next_y]:
                continue
            path.append((next_x, next_y))
            t[next_x][next_y] = True
            stack.append((next_x, next_y))
            break
    pathes = []
    for i in range(k - 1):
        pathes.append([path.pop(), path.pop()])

    pathes.append(path)
    return pathes


ans = proc(n, m, k)
for path in ans:
    if _DEBUG:
        print('{} {}'.format(len(path), ' '.join(map(lambda x: '{} {}'.format(*x), path))))
    else:
        print('{} {}'.format(len(path), ' '.join(map(lambda x: '{} {}'.format(*x), path))) + '\n')
