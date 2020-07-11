import math


def solve(n, x, blows):
    # max_dh = max(d - h for d, h in blows)
    """
    x - (k - 1) * (d - h) - max(d) <= 0
    x - max(d) <= (k - 1) * (d - h)
    (x - max(d)) / (d - h) + 1 <= k

    :param n:
    :param x:
    :param blows:
    :return:
    """

    r = float('inf')
    dh = []
    maxd = max(blows)[0]
    for d, h in blows:
        if d >= x:
            return 1
        elif d <= h:
            continue
        dh.append((d - h, d, h))
        v = int(math.ceil((x - maxd) / (d - h))) + 1
        r = min(r, v)
    if not dh:
        return -1
    return r


for _ in range(int(input())):
    n, x = map(int, input().split())
    blows = []
    for _ in range(n):
        d, h = map(int, input().split())
        blows.append((d, h))
    print(solve(n, x, blows))
