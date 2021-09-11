# https://codeforces.com/contest/1481/problem/C
import sys
from collections import defaultdict

_DEBUG = False
# _DEBUG = True
if not _DEBUG:
    input = sys.stdin.buffer.readline


def solve(n, m, a, b, c):
    color_to_painters = defaultdict(list)
    color_to_idx = {}

    ans = [None] * m
    for i in range(m):
        color = c[i]
        color_to_painters[color].append(i)

    for i in range(n):
        as_is, to_be = a[i], b[i]
        if to_be not in color_to_idx:
            color_to_idx[to_be] = i

        if a[i] == b[i]:
            continue

        if not color_to_painters[to_be]:
            return None
        painter = color_to_painters[to_be].pop()
        ans[painter] = i

    painted_idx = None
    for i in range(m - 1, -1, -1):
        if ans[i] is not None:
            if painted_idx is None:
                painted_idx = ans[i]
            continue

        if painted_idx is not None:
            ans[i] = painted_idx
        elif c[i] in color_to_idx:
            ans[i] = color_to_idx[c[i]]
            if painted_idx is None:
                painted_idx = color_to_idx[c[i]]
        else:
            return None
    ans = [e + 1 for e in ans]
    return ans


if _DEBUG:
    assert solve(3, 3, [2, 2, 2], [2, 2, 2], [2, 3, 2]) == [1, 1, 1]
    assert solve(1, 1, [1], [1], [1]) == [1]
    # assert solve(5, 2, [1, 2, 2, 1, 1], [1, 2, 2, 1, 1], [1, 2]) == [2, 2]
    # assert solve(10, 5, [7, 3, 2, 1, 7, 9, 4, 2, 7, 9], [9, 9, 2, 1, 4, 9, 4, 2, 3, 9], [9, 9, 7, 4, 3]) == [2, 1, 9, 5, 9]
    assert solve(5, 2, [1, 2, 2, 1, 1], [1, 2, 2, 1, 1], [3, 3]) is None
    assert solve(6, 4, [3, 4, 2, 4, 1, 2], [2, 3, 1, 3, 1, 1], [2, 2, 3, 4]) is None

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    ans = solve(n, m, a, b, c)
    if ans is None:
        print('NO')
    else:
        print('YES')
        print(' '.join(map(str, ans)))
