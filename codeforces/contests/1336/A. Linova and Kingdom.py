import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().strip().split())

g = {}

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().strip().split())
    if u not in g:
        g[u] = set()
    if v not in g:
        g[v] = set()
    g[u].add(v)
    g[v].add(u)


def solve(n, k, g):
    if n == k:
        return 0
    if n - 1 == k:
        return k

    depth_dict = defaultdict(int)
    parent_dict = defaultdict(int)
    stack = [(-1, 1, 0)]
    leaves = []
    while stack:
        parent, node, depth = stack.pop()
        parent_dict[node] = parent
        depth_dict[node] = depth
        child_count = 0
        for e in g[node]:
            if e == parent:
                continue
            stack.append((node, e, depth + 1))
            child_count += 1

        if child_count == 0:  # is leaf
            leaves.append(node)

    count_dict = defaultdict(int)
    event_dict = defaultdict(int)
    while leaves:
        nl = set()
        for node in leaves:
            parent = parent_dict[node]
            if parent == -1:
                continue
            count_dict[parent] += (count_dict[node] + 1)
            event_dict[parent] += 1

            if event_dict[parent] == len(g[parent]) - 1:
                nl.add(parent)
        leaves = nl

    h = []
    for i in range(1, n + 1):
        h.append(depth_dict[i] - count_dict[i])
    h.sort(reverse=True)
    sum_of_happiness = 0
    for i in range(k):
        sum_of_happiness += h[i]
    return sum_of_happiness


hapiness = solve(n, k, g)
print(hapiness)
