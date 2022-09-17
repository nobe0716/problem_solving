# 2022-09-17 12:10:29.417022
# https://codeforces.com/problemset/problem/1651/C
import sys
from typing import List

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, a, b):
    def best_idx(arr: List[int], v: int):
        mi = 0
        for i in range(1, n):
            if abs(arr[i] - v) < abs(arr[mi] - v):
                mi = i
        return mi

    def cost(i: int, j: int):
        return abs(a[i] - b[j])

    head_indices = [0, best_idx(b, a[0]), n - 1]  # a[0] to
    tail_indices = [0, best_idx(b, a[-1]), n - 1]  # a[-1] to

    optimal_cost = float('inf')
    for head_index in head_indices:
        for tail_index in tail_indices:
            cur = cost(0, head_index) + cost(-1, tail_index)

            if head_index > 0 and tail_index > 0:
                cur += cost(best_idx(a, b[0]), 0)
            if head_index < n - 1 and tail_index < n - 1:
                cur += cost(best_idx(a, b[-1]), n - 1)

            optimal_cost = min(optimal_cost, cur)

    return optimal_cost


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = proc(n, a, b)
    print(ans)
