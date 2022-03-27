# 2022-03-27 18:47:07.837475
# https://codeforces.com/problemset/problem/1569/C
import sys
from collections import Counter

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write

_MOD = 998244353


def proc(n, a):
    c = Counter(a)
    max_a = max(a)

    facto_to_n = 1
    for i in range(2, n + 1):
        facto_to_n = (facto_to_n * i) % _MOD

    if c[max_a] >= 2:
        return facto_to_n

    k = c[max_a - 1]
    if k == 0:
        return 0

    v = 1
    for i in range(2, n + 1):
        if i == k + 1:
            continue
        v = (v * i) % _MOD

    ans = facto_to_n - v
    if ans < 0:
        ans += _MOD
    return ans


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = proc(n, a)
    print(ans)
