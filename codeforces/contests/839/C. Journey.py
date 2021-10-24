# https://codeforces.com/problemset/problem/839/C
import sys
from collections import defaultdict

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline

g = defaultdict(set)
n = int(input().strip())
for _ in range(n - 1):
    a, b = map(int, input().strip().split())
    g[a].add(b)
    g[b].add(a)

expected_value = 0
length = 0

q = {1: 1.0}

while q:
    nq = defaultdict(float)

    for cur, prob in q.items():
        if len(g[cur]) == 0:
            expected_value += (prob * length)
        for next in g[cur]:
            nq[next] += (prob / len(g[cur]))
            g[next].discard(cur)
        del g[cur]

    length += 1
    q = nq

print(expected_value)
