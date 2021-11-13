# https://codeforces.com/problemset/problem/687/A
import sys
from collections import defaultdict

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, m, g):
    is_red_table = {}
    for i in range(1, n + 1):
        if i in is_red_table:
            continue
        is_red = True

        q = {i}
        is_red_table[i] = is_red
        is_red = not is_red

        while q:
            nq = set()
            for e in q:
                for next in g[e]:
                    if next in is_red_table:
                        if is_red_table[next] != is_red:
                            return None
                        else:
                            continue

                    is_red_table[next] = is_red
                    nq.add(next)
            q = nq
            is_red = not is_red
    reds = []
    blacks = []
    for i in range(1, n + 1):
        if is_red_table[i]:
            reds.append(i)
        else:
            blacks.append(i)
    return reds, blacks


n, m = map(int, input().strip().split())
g = defaultdict(set)
for _ in range(m):
    u, v = map(int, input().strip().split())
    g[u].add(v)
    g[v].add(u)
ans = solve(n, m, g)
if ans is None:
    print(-1)
else:
    reds, blacks = ans
    print(len(reds))
    print(' '.join(map(str, reds)))
    print(len(blacks))
    print(' '.join(map(str, blacks)))
