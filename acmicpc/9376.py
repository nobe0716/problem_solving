# https://www.acmicpc.net/problem/9376
class Edge:
    def __init__(self, edge_from, edge_to):
        self.f = edge_from
        self.t = edge_to


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_adjacent(self):
        x, y = self.x, self.y
        return [Point(x - 1, y), Point(x + 1, y), Point(x, y - 1), Point(x, y + 1)]

    @staticmethod
    def equals(p1, p2):
        return p1.x == p2.x and p1.y == p2.y


class State:
    # doors should contains every valid path, not shortest
    def __init__(self, depth, doors):
        self.d = depth
        self.doors = doors

    @staticmethod
    def is_equal_state(state1, state2):
        if state1.d != state2.d:
            return False
        if len(state1.doors) != len(state2.doors):
            return False
        for p1, p2 in zip(state1.doors, state2.doors):
            if not Point.equals(p1, p2):
                return False
        return True

    @staticmethod
    def alreay_joined_state(states, state):
        for joined_state in states:
            if State.is_equal_state(joined_state, state):
                return True
        return False

class Map:
    PRISONER = '$'
    DOOR = '#'
    WALL = '*'
    LOAD = '.'

    def __init__(self, jail, h, w):
        self.j = jail
        self.h = h
        self.w = w
        self.f = [[100000 for _ in range(w)] for _ in range(h)]

    def in_bound(self, point):
        return 0 <= point.x < self.h and 0 <= point.y < self.w

    def is_prisoner(self, point):
        return self.in_bound(point) and self.j[point.x][point.y] == Map.PRISONER

    def is_load(self, point):
        return self.in_bound(point) and (self.j[point.x][point.y] == Map.LOAD or self.j[point.x][point.y] == Map.PRISONER)

    def is_door(self, point):
        return self.in_bound(point) and self.j[point.x][point.y] == Map.DOOR

    def is_wall(self, point):
        return self.in_bound(point) and self.j[point.x][point.y] == Map.WALL

    def is_edge(self, point):
        return point.x == 0 or point.y == 0 or point.x == self.h - 1 or point.y == self.w - 1

    def is_exit(self, point):
        return self.is_edge(point) and not self.is_wall(point)

    def flood(self):
        # exits = []
        queue = []
        for i in range(h):
            for j in range(w):
                p = Point(i, j)
                if self.is_exit(p):
                    if self.is_door(p):
                        self.f[i][j] = 1
                    else:
                        self.f[i][j] = 0
                    queue.append(p)
        while len(queue) > 0:
            point = queue.pop(0)
            for p in point.get_adjacent():
                if not self.in_bound(p) or self.is_wall(p):
                    continue
                depth = self.f[point.x][point.y]
                if self.is_door(p):
                    depth += 1
                if depth < self.f[p.x][p.y]:
                    self.f[p.x][p.y] = depth
                    queue.append(p)


def print_state_table(table):
    print '-' * 20
    for l in table:
        for s in l:
            print ' ' if s is None else s.d,
        print ''


for _ in range(int(raw_input())):
    h, w = map(int, raw_input().split())
    s = []

    for i in range(h):
        s.append(raw_input())

    m = Map(s, h, w)

    exits = []
    prisoners = []
    for i in range(h):
        for j in range(w):
            p = Point(i, j)
            if m.is_prisoner(p):
                prisoners.append(p)
            if m.is_exit(p):
                exits.append(p)
    m.flood()

    for i in range(h):
        for j in range(w):
            if m.is_prisoner(Point(i, j)):
                print '>%d<' % m.f[i][j],
            else:
                print '   ' if m.f[i][j] > 10000 else '(%d)' % m.f[i][j],
        print ''
    print(m.f[prisoners[0].x][prisoners[0].y])
    print(m.f[prisoners[1].x][prisoners[1].y])