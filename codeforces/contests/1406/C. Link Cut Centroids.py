# 2022-07-24T16:07:52Z
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

_DEBUG = False

if not _DEBUG:
    input = sys.stdin.readline


def proc(n, edges):
    g = defaultdict(set)
    for x, y in edges:
        g[x].add(y)
        g[y].add(x)

    deq = deque([1])
    while deq:
        e = deq.popleft()
        for ne in g[e]:
            g[ne].discard(e)
            deq.append(ne)

    stack = [1]
    calc_order = []
    while stack:
        e = stack.pop()
        for ne in g[e]:
            stack.append(ne)
            calc_order.append((e, ne))

    node_count = [1] * (n + 1)
    for parent, child in calc_order[::-1]:
        node_count[parent] += node_count[child]

    candidates = []
    for e in range(1, n + 1):
        maximum_component_size = max(node_count[v] for v in g[e]) if g[e] else 0
        maximum_component_size = max(maximum_component_size, n - node_count[e])

        candidates.append((maximum_component_size, e))

    candidates.sort()

    if candidates[0][0] < candidates[1][0]:  # already one
        return [edges[0], edges[0]]

    parent, child = candidates[1][1], candidates[0][1]

    if parent in g[child]:
        parent, child = child, parent

    fc = list(g[child])[0]

    return [
        [child, fc], [parent, fc]
    ]


for _ in range(int(input())):
    n = int(input())
    edges = []
    for _ in range(n - 1):
        x, y = map(int, input().split())
        edges.append((x, y))

    ans = proc(n, edges)
    for x, y in ans:
        print(x, y)
