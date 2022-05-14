# 2022-05-14T21:42:23.355Z
from collections import defaultdict, deque


def proc(n, g):
    if n % 2 == 1:
        return -1

    parent = [0] * (n + 1)
    node_count = [1] * (n + 1)
    node_stack = []

    node_queue = deque([1])
    while node_queue:
        node = node_queue.popleft()
        node_stack.append(node)
        for e in g[node]:
            node_queue.append(e)
            g[e].remove(node)
            parent[e] = node

    ans = 0
    while node_stack:
        node = node_stack.pop()
        if node_count[node] % 2 == 0:
            ans += 1
        node_count[parent[node]] += node_count[node]

    # print(parent)
    # print(node_count)
    return ans - 1


g = defaultdict(set)
n = int(input())
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].add(v)
    g[v].add(u)

print(proc(n, g))
