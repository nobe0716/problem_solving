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

...
"""
from collections import namedtuple

_DEBUG = True
num_of_test = int(input())

Point = namedtuple('Point', 'x y')


class People:
    def __init__(self, _point, _direction):
        self.p = _point
        self.d = _direction

    def will_pass(self, point):
        if self.d == 'N':
            return point.y > self.p.y
        elif self.d == 'E':
            return point.x > self.p.x
        elif self.d == 'S':
            return point.y < self.p.y
        else:  # 'W'
            return point.x < self.p.x


def solve(p, q, peoples):
    maximum_val = 0
    maximum_pos = Point(0, 0)

    for i in range(0, q + 1):
        for j in range(0, q + 1):
            point = Point(i, j)
            c = 0
            for people in peoples:
                if people.will_pass(point):
                    c += 1
            if c > maximum_val:
                maximum_val = c
                maximum_pos = point
    return maximum_pos


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
