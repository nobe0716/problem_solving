import sys
from collections import defaultdict, deque
from operator import itemgetter

sys.setrecursionlimit(200000)
_DEBUG = False

if _DEBUG:
    sys.stdin = open('c.in')
else:
    input = sys.stdin.readline


def solve(n: int, edges):
    g = defaultdict(set)
    for a, b in edges:
        g[a].add(b)
        g[b].add(a)
    # nodes = [None, root] + [None] * (n - 1)

    deq = deque([1])

    while deq:
        node = deq.popleft()
        for next in g[node]:
            g[next].remove(node)
            deq.append(next)

    calc_order = []
    stack = [1]
    while stack:
        node = stack.pop()
        for child in g[node]:
            calc_order.append((node, child))
            stack.append(child)

    vertex_count = [0] + [1] * n
    for parent, child in calc_order[::-1]:
        vertex_count[parent] += vertex_count[child]

    candidates = []
    for i in range(1, n + 1):
        largest_child_count = max(vertex_count[child] for child in g[i]) if g[i] else 0
        largest_sub_component_size = max(largest_child_count, n - vertex_count[i])
        candidates.append((largest_sub_component_size, len(g[i]), i))
    candidates.sort(key=itemgetter(0, 1))

    if candidates[0][0] < candidates[1][0]:  # only one centroid
        return [edges[0], edges[0]]

    child = candidates[0][2]
    parent = candidates[1][2]

    if parent in g[child]:
        child, parent = parent, child
    first_child_of_child = list(g[child])[0]
    return [
        [child, first_child_of_child],
        [parent, first_child_of_child]
    ]


for _ in range(int(input())):  # t
    n = int(input())
    edges = []
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edges.append((a, b))

    cuts = solve(n, edges)
    for a, b in cuts:
        print(a, b)
