# 2022-03-12 19:52:17.071947
# https://codeforces.com/problemset/problem/1264/A
import sys
from collections import Counter

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


def proc(n, points):
    c = Counter(points)
    keys = sorted(c.keys(), reverse=True)

    gold = c[keys[0]]
    silver = 0
    bronze = 0

    for point in keys[1:]:
        if gold + silver + bronze >= n // 2:
            break
        if silver <= gold:
            silver += c[point]
        elif gold + silver + bronze + c[point] <= n // 2:
            bronze += c[point]
        else:
            break

    if gold >= silver or gold >= bronze or silver == 0 or bronze == 0 or gold + silver + bronze > n // 2:
        return 0, 0, 0
    return gold, silver, bronze


for _ in range(int(input())):
    n = int(input())
    points = list(map(int, input().split()))
    ans = proc(n, points)
    if _DEBUG:
        print(' '.join(map(str, ans)))
    else:
        print(' '.join(map(str, ans)) + '\n')
