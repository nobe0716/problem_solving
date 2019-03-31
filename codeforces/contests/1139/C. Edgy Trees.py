_MOD = 10 ** 9 + 7
from collections import defaultdict

n, k = map(int, input().split())
g = defaultdict(dict)
for _ in range(n - 1):
    u, v, x = map(int, input().split())
    g[u][v] = g[v][u] = x

visited_vertex = set()
groups = []
for i in range(1, n + 1):
    if i in visited_vertex:
        continue
    # groups.append(find_group(i, g))
    s = [i]
    visited_vertex.add(i)
    group = {i}
    while len(s) > 0:
        e = s.pop()
        # visited_vertex.add(e)
        for next in g[e]:
            if next in visited_vertex or g[e][next] == 1:
                continue
            s.append(next)
            visited_vertex.add(next)
            group.add(next)
    groups.append(group)

r = n ** k
for group in groups:
    r -= (len(group) ** k)
print(r % _MOD)
