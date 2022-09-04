# 2022-08-27 19:49:22.850449
# https://codeforces.com/problemset/problem/1646/C
import bisect
import math
import sys
from functools import lru_cache

sys.setrecursionlimit(10000)
_LIMIT = 10 ** 12

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write

power_of_two = [2 ** i for i in range(int(math.log2(_LIMIT) + 1))]
set_power_of_tw = set(power_of_two)

f = 1
v = 2
factorials = []
while f <= _LIMIT:
    f *= v
    factorials.append(f)
    v += 1
set_factorials = set(factorials)


@lru_cache(None)
def proc(n, max_idx_t=len(power_of_two), max_idx_f=len(factorials)):
    if n in set_factorials or n in set_power_of_tw:
        return 1
    if n < 0 or (max_idx_t == 0 and max_idx_f == 0):
        return float('inf')
    if n == 0:
        return 0

    # print(n, max_idx_t, max_idx_f)

    idx_t = bisect.bisect(power_of_two, n, hi=max_idx_t) - 1
    idx_f = bisect.bisect(factorials, n, hi=max_idx_f) - 1

    res = float('inf')

    if power_of_two[idx_t] >= factorials[idx_f]:
        return proc(n - power_of_two[idx_t], idx_t, max_idx_f) + 1
    else:
        return proc(n - factorials[idx_f], max_idx_t, idx_f) + 1


# v = proc(240)
# print(v)
# assert v == 4

for _ in range(int(input())):
    n = int(input())
    ans = proc(n)
    print(ans)
