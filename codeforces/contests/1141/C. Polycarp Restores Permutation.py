# 2022-02-20 15:31:20.582048
# https://codeforces.com/problemset/problem/1141/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def proc(n, a):
    b = [0]
    for e in a:
        b.append(b[-1] + e)
    k = 1 - min(b)

    for i in range(n):
        b[i] += k

    if sorted(b) == list(range(1, n + 1)):
        return b
    return [-1]


n = int(input())
a = list(map(int, input().split()))
ans = proc(n, a)
print(' '.join(map(str, ans)))
