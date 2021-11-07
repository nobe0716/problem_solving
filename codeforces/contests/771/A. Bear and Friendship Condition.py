# https://codeforces.com/problemset/problem/771/A
import sys
from collections import defaultdict

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, m, g):
    visited = set()
    for i in range(1, n + 1):
        if i in visited:
            continue

        visited.add(i)
        stack = [i]

        group = {i}
        while stack:
            e = stack.pop()
            for v in g[e]:
                if v in visited:
                    continue
                visited.add(v)
                group.add(v)
                stack.append(v)

        group_size = len(group)
        cnt = sum(len(g[e]) for e in group) // 2

        if cnt != group_size * (group_size - 1) // 2:
            if _DEBUG:
                print(group_size, cnt, group)
            return False
    return True


n, m = map(int, input().strip().split())
g = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().strip().split())
    g[a].add(b)
    g[b].add(a)

ans = solve(n, m, g)
print('YES' if ans else 'NO')
