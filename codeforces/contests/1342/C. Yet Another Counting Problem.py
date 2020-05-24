import functools
import math
import sys

# sys.stdin = open('c.in')
t = int(sys.stdin.readline())


def solve(a, b, queries):
    if a > b:
        a, b = b, a
    gcd = math.gcd(a, b)
    lcm = gcd * (a // gcd) * (b // gcd)
    result = []

    @functools.lru_cache(None)
    def count_to_x(x):
        if x < lcm:
            return 0 if x < b else x - b + 1
        else:
            r = (x // lcm) * b + min(x - (x // lcm * lcm) + 1, b)
        return (x + 1) - r

    for li, ri in queries:
        result.append(count_to_x(ri) - count_to_x(li - 1))
    return result


for _ in range(t):
    a, b, q = map(int, sys.stdin.readline().split())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, sys.stdin.readline().split())))
    r = solve(a, b, queries)
    print(' '.join(map(str, r)))
