# https://codeforces.com/problemset/problem/1325/C
import sys
from collections import defaultdict

_DEBUG = True
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline

n = int(input())
g = defaultdict(list)
edge_no = dict()
for i in range(n - 1):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    edge_no[(a, b)] = i
    g[a].append(b)
    g[b].append(a)

edges_to_num = [None] * (n - 1)
for i in range(1, n + 1):
    if len(g[i]) >= 3:
        v1, v2, v3 = g[i][0], g[i][1], g[i][2]
        edge1 = edge_no[min(i, v1), max(i, v1)]
        edge2 = edge_no[min(i, v2), max(i, v2)]
        edge3 = edge_no[min(i, v3), max(i, v3)]

        edges_to_num[edge1] = 0
        edges_to_num[edge2] = 1
        edges_to_num[edge3] = 2
        break

if all(x is None for x in edges_to_num):
    edges_to_num = list(range(n - 1))
else:
    j = 3
    for i in range(n - 1):
        if edges_to_num[i] is None:
            edges_to_num[i] = j
            j += 1

print('\n'.join(map(str, edges_to_num)))
