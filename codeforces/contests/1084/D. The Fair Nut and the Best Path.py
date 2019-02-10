"""
WIP
"""
import sys
from collections import defaultdict

sys.setrecursionlimit(30002)
n = int(input())
w = [0] + list(map(int, input().split()))
g = defaultdict(dict)
for _ in range(n - 1):
    u, v, c = map(int, input().split())
    g[v][u] = g[u][v] = c

max_idx = 0
max_gas = 0
for i, gas in enumerate(w):
    if gas > max_gas:
        max_idx = i
        max_gas = gas


def fill_table(node, parent, gas, t):
    # print(node, gasoline, last_visited)
    gas += w[node]
    candidates = [gas]
    for n, c in g[node].items():
        if n == parent:
            continue
        if gas >= c:
            fill_table(n, node, gas - c, t)
            candidates.append(t[n])
    t[node] += max(candidates)


r = []
for i in range(1, n + 1):
    dp = [0] * (n + 1)
    fill_table(i, 0, 0, dp)
    r.append(dp[i])
print(max(r))
