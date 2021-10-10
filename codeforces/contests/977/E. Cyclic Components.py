# https://codeforces.com/problemset/problem/977/E
import sys
from collections import defaultdict

sys.setrecursionlimit(200005)
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def clean_graph(start):
    stack = [start]
    while stack:
        v = stack.pop()
        stack += g[v]
        g[v] = []


for i in range(n + 1):
    if len(g[i]) != 2:
        clean_graph(i)

ans = 0
for i in range(n + 1):
    if g[i]:
        clean_graph(i)
        ans += 1
print(ans)
