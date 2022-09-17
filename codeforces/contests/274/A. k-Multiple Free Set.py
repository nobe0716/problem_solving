# 2022-09-17 16:27:22.421726
# https://codeforces.com/problemset/problem/274/A
import sys
from collections import Counter

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, k, a):
    a = sorted(a)
    s = set(a)
    visited = set()
    group_cnt = 0

    for e in a:
        if e in visited:
            continue
        group_cnt += 1

        if e * k in s:
            visited.add(e * k)

    return group_cnt


n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = proc(n, k, a)
print(ans)
