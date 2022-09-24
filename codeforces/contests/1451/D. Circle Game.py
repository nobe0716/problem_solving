# 2022-09-24 16:07:54.107353
# https://codeforces.com/problemset/problem/1451/D
import sys
from math import sqrt

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(d, k):
    bound = sqrt(d ** 2 / 2)
    times = bound // k

    i = 0
    p = q = 0
    while p ** 2 + q ** 2 <= d ** 2:
        if i % 2 == 0:
            p += k
        else:
            q += k
        i += 1
    return True if i % 2 == 1 else False


for _ in range(int(input())):
    d, k = map(int, input().split())
    ans = proc(d, k)

    print('Utkarsh' if ans else 'Ashish')
