# 2022-08-15 23:22:25.776455
# https://codeforces.com/problemset/problem/742/B
import sys
from collections import Counter

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, x, a):
    c = Counter()
    ans = 0
    for e in a:
        ans += c[e ^ x]
        c[e] += 1
    return ans


n, x = map(int, input().split())
a = list(map(int, input().split()))

print(proc(n, x, a))
