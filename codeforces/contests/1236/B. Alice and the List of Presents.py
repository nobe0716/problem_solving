# 2022-03-12 16:22:54.012302
# https://codeforces.com/problemset/problem/1236/B
import sys

_MOD = (10 ** 9 + 7)

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, m):
    base = (pow(2, m, _MOD) - 1) % _MOD
    return pow(base, n, _MOD)


n, m = map(int, input().split())
print(proc(n, m))
