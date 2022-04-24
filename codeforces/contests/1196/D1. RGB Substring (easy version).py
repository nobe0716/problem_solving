# 2022-04-24 18:39:58.616536
# https://codeforces.com/problemset/problem/1196/D1
import sys

_DEBUG = True
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, k, s):
    t = [[0] * (n + 1) for _ in range(3)]

    for i, p in enumerate(('RGB', 'GBR', 'BRG')):
        for j in range(n):
            t[i][j + 1] = t[i][j]

            if p[j % 3] != s[j]:
                t[i][j + 1] += 1

    ans = float('inf')
    for i in range(3):
        for j in range(k, n + 1):
            ans = min(ans, t[i][j] - t[i][j - k])
    return ans


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ans = proc(n, k, s)
    print(ans)
