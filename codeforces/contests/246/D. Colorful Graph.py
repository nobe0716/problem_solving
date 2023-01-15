import sys
from collections import defaultdict

_DEBUG = True
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write

g = defaultdict(set)
n, m = map(int, input().split())
c = [0] + list(map(int, input().split()))
colors = set(c[1:])
for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)

diversity = defaultdict(set)

visited = set()
for i in range(n + 1):
    if i in visited:
        continue
    visited.add(i)
    q = [i]
    while q:
        nq = []
        for e in q:
            color = c[e]

            for ne in g[e]:
                new_color = c[ne]
                if new_color != color:
                    diversity[new_color].add(color)
                    diversity[color].add(new_color)
                if ne in visited:
                    continue
                visited.add(ne)
                nq.append(ne)
        q = nq

max_color = None
for color in colors:
    if max_color is None:
        max_color = color
    if len(diversity[color]) > len(diversity[max_color]):
        max_color = color
    elif len(diversity[color]) == len(diversity[max_color]):
        max_color = min(max_color, color)
print(max_color)
