import math

n, m, q = map(int, input().split())
gcd = math.gcd(n, m)
gn = n // gcd
gm = m // gcd


def get_pos(p):
    if p[0] == 1:
        return (p[1] - 1) // gn
    return (p[1] - 1) // gm


def possible(start, end):
    start_pos = get_pos(start)
    end_pos = get_pos(end)
    return start_pos == end_pos


for _ in range(q):
    sx, sy, ex, ey = map(int, input().split())
    r = possible((sx, sy), (ex, ey))
    print('YES' if r else 'NO')
