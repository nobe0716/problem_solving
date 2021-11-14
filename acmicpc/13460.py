import functools
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solve(n, m, g):
    @functools.lru_cache(None)
    def move(x: int, y: int, d: Direction):
        nx, ny = x, y
        while 0 < nx + dx[d.value] <= n and 0 < ny + dy[d.value] <= m and g[nx + dx[d.value]][ny + dy[d.value]] != '#':
            nx += dx[d.value]
            ny += dy[d.value]

            if nx == HOLE[0] and ny == HOLE[1]:
                break

        return nx, ny

    def tilt(rx, ry, bx, by, dir: Direction):
        nrx, nry = move(rx, ry, dir)
        nbx, nby = move(bx, by, dir)
        if nrx != nbx or nry != nby:
            return nrx, nry, nbx, nby
        if nrx == HOLE[0] and nry == HOLE[1]:
            return None

        if Direction.UP == dir:
            if rx < bx:
                nbx += 1
            else:
                nrx += 1
        elif Direction.DOWN == dir:
            if rx > bx:
                nbx -= 1
            else:
                nrx -= 1
        elif Direction.LEFT == dir:
            if ry < by:
                nby += 1
            else:
                nry += 1
        else:  # Direction.RIGHT == dir
            if ry > by:
                nby -= 1
            else:
                nry -= 1

        return nrx, nry, nbx, nby

    rx = ry = bx = by = 0
    HOLE = None

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if g[i][j] == 'O':
                HOLE = i, j
            elif g[i][j] == 'R':
                rx, ry = i, j
                g[i][j] = '.'
            elif g[i][j] == 'B':
                bx, by = i, j
                g[i][j] = '.'

    q = [(rx, ry, bx, by)]
    v = {(rx, ry, bx, by)}

    for i in range(10):
        nq = set()
        for rx, ry, bx, by in q:
            for dir in Direction:
                tilt_res = tilt(rx, ry, bx, by, dir)
                if not tilt_res:
                    continue
                nrx, nry, nbx, nby = tilt_res
                if nbx == HOLE[0] and nby == HOLE[1]:
                    continue
                if tilt_res in v:
                    continue
                if nrx == HOLE[0] and nry == HOLE[1]:
                    return i + 1

                v.add(tilt_res)
                nq.add(tilt_res)
        q = nq
    return -1


n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]

print(solve(n, m, g))
