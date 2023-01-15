# 2023-01-16 00:52:25.930074
# https://codeforces.com/problemset/problem/1536/C
import math
import sys
from collections import defaultdict, Counter

_DEBUG = False
_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, s):
    t = defaultdict(int)
    res = []

    c = Counter()
    for e in s:

        c[e] += 1

        if c['D'] == 0:
            key = (0, 1)
        elif c['K'] == 0:
            key = (1, 0)
        else:
            g = math.gcd(c['D'], c['K'])
            key = (c['D'] // g, c['K'] // g)

        t[key] += 1
        res.append(t[key])

    return res


for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = proc(n, s)
    print(' '.join(map(str, ans)))
