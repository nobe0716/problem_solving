# 2022-03-05 15:25:19.497954
# https://codeforces.com/problemset/problem/1466/D
import sys
from collections import defaultdict, deque

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, costs, edges):
    costs = [0] + costs
    g = defaultdict(int)
    for a, b in edges:
        g[a] += 1
        g[b] += 1

    res = [sum(costs)]

    candidates = deque(sorted(filter(lambda x: g[x] > 1, range(1, n + 1)), key=lambda x: costs[x], reverse=True))

    for _ in range(n - 2):
        if not candidates:
            res.append(res[-1])

        i = candidates[0]
        res.append(res[-1] + costs[i])
        g[i] -= 1
        if g[i] == 1:
            candidates.popleft()

    return res


if _DEBUG:
    assert proc(4, [10, 6, 6, 6], [(1, 2), (2, 3), (4, 1)]) == [28, 38, 44]
    # assert proc(4, [0, 3, 5, 4, 6], [(2, 1), (3, 1), (4, 3)]) == [18, 22, 25]

for _ in range(int(input())):
    n = int(input())
    costs = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    ans = proc(n, costs, edges)
    print(' '.join(map(str, ans)))
