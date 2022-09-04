# 2022-09-04 12:35:14.236880
# https://codeforces.com/problemset/problem/1516/C
import sys
from collections import Counter

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, a):
    sa = sum(a)

    t = set()
    for e in a:
        for v in list(t):
            t.add(v + e)
        t.add(e)

    if sa % 2 == 1 or (sa // 2) not in t:
        return None

    while True:
        for i, e in enumerate(a):
            if e % 2:
                return i + 1
        a = [e // 2 for e in a]
    return 1


n = int(input())
a = list(map(int, input().split()))
ans = proc(n, a)
if not ans:
    print(0)
else:
    print(1)
    print(ans)
