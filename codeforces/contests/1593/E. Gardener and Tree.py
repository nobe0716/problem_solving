from collections import defaultdict


def proc(n, k, edges):
    if k >= n:
        return 0

    g = defaultdict(set)
    for u, v in edges:
        g[u].add(v)
        g[v].add(u)

    vertex_to_weight = defaultdict(int)

    q = []
    w = 1
    for e in range(1, n + 1):
        if len(g[e]) != 1:
            continue
        vertex_to_weight[e] = w

        q.append(e)

    while q:
        w += 1
        nq = []

        candidates = set()
        for e in q:
            for ne in g[e]:
                g[ne].discard(e)
                candidates.add(ne)
        for e in candidates:
            if len(g[e]) <= 1 and e not in vertex_to_weight:
                vertex_to_weight[e] = w
                nq.append(e)
        q = nq

    res = n
    for e in range(1, n + 1):
        if vertex_to_weight[e] <= k:
            res -= 1
    return res


for _ in range(int(input())):
    input()
    n, k = map(int, input().split())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    ans = proc(n, k, edges)
    print(ans)
