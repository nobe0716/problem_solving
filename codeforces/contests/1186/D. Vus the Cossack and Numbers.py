# 2022-11-06 23:18:20.065822
# https://codeforces.com/problemset/problem/1186/D
import math
import sys

_DEBUG = False
_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, a):
    b = [int(math.floor(x)) for x in a]
    sb = sum(b)

    for i in range(n):
        if sb == 0:
            break
        v = math.ceil(a[i])
        if b[i] != v:
            sb = sb - b[i] + v
            b[i] = v

    return b


n = int(input())
a = []
for _ in range(n):
    a.append(float(input()))

b = proc(n, a)
print('\n'.join(map(str, b)))
