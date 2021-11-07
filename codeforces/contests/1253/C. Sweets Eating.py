# https://codeforces.com/problemset/problem/1253/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, m, a):
    a = sorted(a)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
    table = [0] * (n + 1)
    for i in range(1, n + 1):
        table[i] = prefix_sum[i] + table[max(0, i - m)]

    return ' '.join(map(str, table[1:]))


n, m = map(int, input().split())
a = list(map(int, input().split()))

print(solve(n, m, a))
