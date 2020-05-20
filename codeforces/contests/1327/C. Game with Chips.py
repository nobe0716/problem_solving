"""
https://codeforces.com/contest/1327/problem/C
"""
import sys
from enum import Enum

_DIRECTION_NAMES = 'URDL'


class Dir(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def apply_moves(self, moves):
        self.x = max(1, self.x - moves[Dir.UP])
        self.y = min(m, self.y + moves[Dir.RIGHT])
        self.x = min(n, self.x + moves[Dir.DOWN])
        self.y = max(1, self.y - moves[Dir.LEFT])


# Up,Right,Down,Left
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m, k = map(int, sys.stdin.readline().strip().split())
src_pos = []
dst_pos = []
for _ in range(k):
    x, y = map(int, sys.stdin.readline().strip().split())
    src_pos.append(Point(x, y))
for _ in range(k):
    x, y = map(int, sys.stdin.readline().strip().split())
    dst_pos.append(Point(x, y))


def solve(n, m, k, src_pos, dst_pos):
    max_x = max_y = 0
    for src in src_pos:
        max_x = max(max_x, src.x)
        max_y = max(max_y, src.y)
    r = 'U' * (max_x - 1) + 'L' * (max_y - 1)
    for i in range(n):
        if i % 2 == 0:
            r += 'R' * (m - 1)
        else:
            r += 'L' * (m - 1)
        if i != n - 1:
            r += 'D'
    return r


r = solve(n, m, k, src_pos, dst_pos)
if r is None:
    print(-1)
else:
    print('{}'.format(len(r)))
    if len(r) > 0:
        print(r)
