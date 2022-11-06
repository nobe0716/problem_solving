# 2022-11-06 23:57:09.614033
# https://codeforces.com/problemset/problem/1482/C
import math
import sys
from collections import Counter

_DEBUG = False
# _DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, m, members):
    occurrence = Counter()
    limit = int(math.ceil(m / 2))

    groups = sorted(enumerate(members), key=lambda x: len(x[1]))

    res = [None] * m
    for idx, members in groups:
        selected_member = sorted(members, key=lambda x: occurrence[x])[0]
        occurrence[selected_member] += 1
        if occurrence[selected_member] > limit:
            return None
        res[idx] = selected_member
    return res


for _ in range(int(input())):
    n, m = map(int, input().split())
    members = []
    for _ in range(m):
        a = list(map(int, input().split()))
        f = a[1:]
        members.append(f)

    ans = proc(n, m, members)
    if not ans:
        print('NO')
    else:
        print('YES')
        print(' '.join(map(str, ans)))

"""
2
4 6
1  1
2  1 2
3  1 2 3
4  1 2 3 4
2  2 3
1  3

2 2
1 1
1 1
"""
