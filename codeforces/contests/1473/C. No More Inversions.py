# 2022-08-20 23:26:50.439209
# https://codeforces.com/problemset/problem/1473/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write

"""
3 2
4 3

1 2 1
1 2 3 2
"""


def proc(n, k):
    a = []
    for i in range(1, k):
        a.append(i)
    for i in range(k, k - (n - k) - 1, -1):
        a.append(i)
    used = set()
    b = []
    for e in a[::-1]:
        if e in used:
            continue
        used.add(e)
        b.append(e)

    return b[::-1]


for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = proc(n, k)
    print(' '.join(map(str, ans)))
