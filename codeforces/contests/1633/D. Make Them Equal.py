# 2022-08-28 21:48:29.252397
# https://codeforces.com/problemset/problem/1633/D
import sys
from collections import defaultdict
from functools import lru_cache

sys.setrecursionlimit(100000)

_DEBUG = True
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write

cost_table = defaultdict(int)
cost_table[1] = 0

q = [1]
while q:
    nq = []
    for s in q:
        for delta in range(1, s + 1):
            key = s + s // delta
            if key in cost_table or key > 1000:
                continue
            cost_table[key] = cost_table[s] + 1
            nq.append(key)
    q = nq


t = [[0] * 12001 for _ in range(1000)]


def proc(n, k, b, c):
    if k >= 12 * n:
        return sum(c)

    acc_sum = list(c)
    for i in range(1, n):
        acc_sum[i] += acc_sum[i - 1]

    for i in range(n):
        for j in range(k + 1):
            t[i][j] = 0

    def dp(idx, budget):
        if idx == -1:
            return 0
        if budget >= 12 * (idx + 1):
            return acc_sum[idx]
        if t[idx][budget]:
            return t[idx][budget]

        current_cost = cost_table[b[idx]]

        ans = 0
        if current_cost <= budget:
            ans = dp(idx - 1, budget - current_cost) + c[idx]
        ans = max(ans, dp(idx - 1, budget))
        t[idx][budget] = ans
        return ans

    return dp(n - 1, k)


for _ in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = proc(n, k, b, c)
    if _DEBUG:
        print(ans)
    else:
        print('{}\n'.format(ans))