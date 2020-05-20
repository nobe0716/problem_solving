import sys
from collections import namedtuple

AB = namedtuple('AB', ['a', 'b'])
t = int(sys.stdin.readline().strip())


def solve(n, abs):
    rest_points = 0
    min_rest_point = float('inf')
    for i in range(n):
        a, b = abs[i].a, abs[i - 1].b
        if a > b:
            rest_points += (a - b)
            min_rest_point = min(min_rest_point, b)
        else:
            min_rest_point = min(min_rest_point, a)

    return rest_points + min_rest_point


responses = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    abs = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().strip().split())
        abs.append(AB(a, b))

    r = solve(n, abs)
    responses.append(r)
print('\n'.join(map(str, responses)))
