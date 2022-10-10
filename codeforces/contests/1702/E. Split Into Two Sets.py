# 2022-10-10 15:10:22.714244
# https://codeforces.com/problemset/problem/1702/E
import sys
from collections import defaultdict

sys.setrecursionlimit(1 * 10 ** 5)
# _DEBUG = True
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


def proc(n, dominos):
    def count(i):
        next = i
        c = 1
        while next:
            x = next
            next = None
            for e in g[x]:
                if e in visited:
                    continue
                visited.add(e)
                next = e
                c += 1
                break
        return c

    g = defaultdict(list)

    for a, b in dominos:
        g[a].append(b)
        g[b].append(a)

        if len(g[a]) > 2 or len(g[b]) > 2:
            return False

    visited = set()
    for i in range(1, n + 1):
        if i in visited:
            continue
        visited.add(i)

        if count(i) % 2 == 1:
            return False
    return True


if _DEBUG:
    assert proc(8, [(2, 1), (1, 2), (4, 3), (4, 3), (5, 6), (5, 7), (8, 6), (7, 8)]) == True
    assert proc(6, [(1, 2), (4, 5), (1, 3), (4, 6), (2, 3), (5, 6)]) == False
    assert proc(8, [(1, 2), (2, 1), (4, 3), (5, 3), (5, 4), (6, 7), (8, 6), (7, 8)]) == False

for _ in range(int(input())):
    n = int(input())
    dominos = []
    for _ in range(n):
        a, b = map(int, input().split())
        dominos.append((a, b))

    ans = proc(n, dominos)
    if _DEBUG:
        print('YES' if ans else 'NO')
    else:
        print('YES\n' if ans else 'NO\n')
