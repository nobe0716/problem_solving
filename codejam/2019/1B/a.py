"""
## Name of Prob
Manhattan Crepe Cart

## Link
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/000000000012295c

## Note

grid (x 0... Q, y 0... Q) inclusive
smallest x coordinate, smallest y coordinates

### direction
North: increasing y direction
South: decreasing y direction
East: increasing x direction
West: decreasing x direction

Q|
 |
 |
 |
0|-------------
 0           Q

## Input

P Q : num of people, grid size
x_i y_i d_i : initial (x, y) and direction

there must be a one move for each people

1 <= T <= 100
1 <= P <= 500

Q = 10 for small
Q = 10^5 for large

## Output

## Strategy

### Simple
Just calculate num of passing people for all grid (0, 0), (0, 1) (0, 2)...(Q, Q-1),(Q, Q)

### Large
Divide grid to X-axis and Y-axis
Then calculate 1-D interval [i, j] which has maximum number of possible intersection

- X-axis
  - filter people whose direction is East or West
  - order people by X-position
  - for pos i, find max(number of E-people whose x is less than i) + (number of W-people whose x is larger than i)
- Y-axis
  - filter people hose direction is North or South
  - order people by Y-position
  - for pos j, find max(number of N-people whose y is less than i) + (number of S-people whose y is larger than j)

"""
from collections import namedtuple, Counter, defaultdict

_DEBUG = True
num_of_test = int(input())

Point = namedtuple('Point', 'x y')


class People:
    def __init__(self, _point, _direction):
        self.pos = _point
        self.dir = _direction

    def will_pass(self, point):
        if self.dir == 'N':
            return point.y > self.pos.y
        elif self.dir == 'E':
            return point.x > self.pos.x
        elif self.dir == 'S':
            return point.y < self.pos.y
        else:  # 'W'
            return point.x < self.pos.x


def solve(p, q, peoples):
    tot_dir_cnt = Counter()
    cur_dir_cnt = Counter()

    ew_cnt = defaultdict(lambda: defaultdict(int))  # pos -> {dir -> count}
    ns_cnt = defaultdict(lambda: defaultdict(int))  # pos -> {dir -> count}
    for p in peoples:
        tot_dir_cnt[p.dir] += 1
        if p.dir == 'N':
            ns_cnt[p.pos.y + 1][p.dir] += 1
        elif p.dir == 'S':
            ns_cnt[p.pos.y][p.dir] += 1
        elif p.dir == 'E':
            ew_cnt[p.pos.x + 1][p.dir] += 1
        else:
            ew_cnt[p.pos.x][p.dir] += 1

    x_pos_max = 0
    x_pos_val = tot_dir_cnt['W']

    for x in sorted(ew_cnt.keys()):
        cur_dir_cnt['E'] += ew_cnt[x]['E']
        cur_dir_cnt['W'] += ew_cnt[x]['W']

        if cur_dir_cnt['E'] + (tot_dir_cnt['W'] - cur_dir_cnt['W']) > x_pos_val:
            x_pos_max = x
            x_pos_val = cur_dir_cnt['E'] + (tot_dir_cnt['W'] - cur_dir_cnt['W'])

    y_pos_max = 0
    y_pos_val = tot_dir_cnt['S']

    for y in sorted(ns_cnt.keys()):
        cur_dir_cnt['N'] += ns_cnt[y]['N']
        cur_dir_cnt['S'] += ns_cnt[y]['S']

        if cur_dir_cnt['N'] + (tot_dir_cnt['S'] - cur_dir_cnt['S']) > y_pos_val:
            y_pos_max = y
            y_pos_val = cur_dir_cnt['N'] + (tot_dir_cnt['S'] - cur_dir_cnt['S'])

    return Point(x_pos_max, y_pos_max)


for test_num in range(1, num_of_test + 1):
    solution = None
    p, q = map(int, input().split())
    peoples = []
    for _ in range(p):
        x, y, d = input().split()
        peoples.append(People(Point(int(x), int(y)), d))

    r = solve(p, q, peoples)
    solution = '{} {}'.format(r.x, r.y)
    print("Case #{}: {}".format(test_num, solution))
