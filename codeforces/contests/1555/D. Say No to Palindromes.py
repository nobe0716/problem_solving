# 2022-04-23 22:29:55.573114
# https://codeforces.com/problemset/problem/1555/D
import itertools
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write

n, m = map(int, input().split())
s = input()

t = [[0] * (n + 1) for _ in range(6)]

for i, cur in enumerate(itertools.permutations('abc', 3)):
    # t[i][0] = 1 if s[0] == cur[0] else 0
    for j in range(0, n):
        t[i][j + 1] = t[i][j]
        if s[j] != cur[j % 3]:
            t[i][j + 1] += 1

for _ in range(m):
    l, r = map(int, input().split())
    ans = min(t[i][r] - t[i][l - 1] for i in range(6))
    print(ans)
