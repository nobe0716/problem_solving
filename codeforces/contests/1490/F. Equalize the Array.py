# https://codeforces.com/problemset/problem/1490/F
"""
C; number's occurrence zero or C

given C, cnt[i]; number of occurrence of i

cost(c) = sum { cnt[i] - C if cnt[i] >= C else cnt[i] }
T = O(N ** 2) without memoization


some tables for memoization, change concept of cnt

cnt[i]; number of distinct elements whose occurrence is exactly i

acc_cnt[i]; acc sum of count of numbers whose occurrence is [0,i]
acc_cnt[i] = acc_cnt[i - 1] + cnt[i]
cost[c] = n - i * (acc_cnt[-1] - acc_cnt[i - 1])

"""
import sys
from collections import Counter
from typing import List

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n: int, a: List[int]) -> int:
    cnt = Counter()
    for k, v in Counter(a).items():
        cnt[v] += 1
    max_limit = max(cnt.keys()) + 1

    acc_cnt = [0] * max_limit
    for i in range(1, max_limit):
        acc_cnt[i] = acc_cnt[i - 1] + cnt[i]

    res = float('inf')

    for i in range(max_limit):
        v = n - i * (acc_cnt[-1] - acc_cnt[i - 1])
        res = min(res, v)
    return res


# assert solve(8, [1, 2, 3, 3, 3, 2, 6, 6]) == 2
# assert solve(6, [1, 3, 2, 1, 4, 2]) == 2
# assert solve(4, [100, 100, 4, 100]) == 1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(n, a)
    print(ans)
