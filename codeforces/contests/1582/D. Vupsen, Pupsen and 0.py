# 2022-10-10 19:55:18.608068
# https://codeforces.com/problemset/problem/1582/D
import math
import sys

_DEBUG = False
_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, a):
    res = []
    # a[i] * b[i] + a[i + 1] + b[i + 1] == 0
    # b[i] = -a[i + 1], b[i + 1] = a[i]
    for i in range(0, n // 2 * 2, 2):
        g = math.gcd(a[i], a[i + 1])
        res.append(-a[i + 1] // g)
        res.append(a[i] // g)
    if n % 2 == 0:
        return res

    res.pop()
    res.pop()
    if a[-3] + a[-2] != 0:
        res += [-a[-1], -a[-1], a[-3] + a[-2]]
    elif a[-3] + a[-1] != 0:
        res += [-a[-2], a[-3] + a[-1], -a[-2]]
    else:  # a[-2] + a[-1] != 0
        res += [a[-2] + a[-1], -a[-3], -a[-3]]

    g = math.gcd(math.gcd(res[-3], res[-2]), res[-1])
    res[-3], res[-2], res[-1] = res[-3] // g, res[-2] // g, res[-1] // g
    return res


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = proc(n, a)
    if _DEBUG:
        print(' '.join(map(str, ans)))
    else:
        print(' '.join(map(str, ans)) + '\n')
