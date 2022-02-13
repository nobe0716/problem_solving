# https://codeforces.com/problemset/problem/1263/D
# 22:13
import sys
from collections import defaultdict

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, passwords):
    g = defaultdict(set)
    # password_sets = list(map(set, passwords))

    global_set = set()
    for password in passwords:
        for e in password:
            global_set.add(e)
            g[password[0]].add(e)
            g[e].add(password[0])

    visited = set()
    c = 0

    for e in global_set:
        if e in visited:
            continue
        c += 1
        stack = [e]
        while stack:
            v = stack.pop()
            for nv in g[v]:
                if nv in visited:
                    continue
                visited.add(nv)
                stack.append(nv)
    return c


# assert solve(4, ['a', 'ac', 'b', 'cb']) == 1

n = int(input())
passwords = [input().strip() for _ in range(n)]
ans = solve(n, passwords)
print(ans)
