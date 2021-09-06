# https://codeforces.com/contest/427/problem/C
import sys
from collections import defaultdict, deque
# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/misc/bootstrap.py

from types import GeneratorType


def bootstrap(to, stack=[]):
    while True:
        if type(to) is GeneratorType:
            stack.append(to)
            to = next(to)
        else:
            stack.pop()
            if not stack:
                break
            to = stack[-1].send(to)
    return to


input = sys.stdin.buffer.readline
n = int(input())
costs = [None] + [int(x) for x in input().strip().split()]
m = int(input())

g = defaultdict(set)
r = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().split())
    g[u].add(v)
    r[v].add(u)

visited = [False] * (n + 1)
assigned = [False] * (n + 1)


def visit(u: int):
    if visited[u]:
        yield
    visited[u] = True
    for v in g[u]:
        yield visit(v)
    l.appendleft(u)
    yield


def assign(u: int, root: int):
    if assigned[u]:
        yield
    assigned[u] = True
    scc.append(u)
    for v in r[u]:
        yield assign(v, root)
    yield


l = deque()
for i in range(1, n + 1):
    bootstrap(visit(i))

total_cost = 0
total_count = 1
_MOD = 1000000007

for u in l:
    scc = []
    bootstrap(assign(u, u))
    if scc:
        min_cost = min(costs[x] for x in scc)
        min_count = sum(1 if costs[x] == min_cost else 0 for x in scc)
        total_cost += min_cost
        total_count *= min_count
        total_count %= _MOD

print(total_cost, total_count)
