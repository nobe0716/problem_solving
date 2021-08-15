# https://codeforces.com/contest/1519/problem/D
# TLE

import sys

input = sys.stdin.readline


def solve(n, a, b):
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i] * b[i]

    max_sum = prefix_sum[-1]
    for i in range(n):
        mid_sum = a[i] * b[i]
        l, r = i - 1, i + 1
        while 0 <= l and r < n:
            mid_sum += a[l] * b[r] + a[r] * b[l]
            max_sum = max(max_sum, prefix_sum[l] + mid_sum + prefix_sum[-1] - prefix_sum[r + 1])
            l -= 1
            r += 1

        mid_sum = 0
        l, r = i, i + 1
        while 0 <= l and r < n:
            mid_sum += a[l] * b[r] + a[r] * b[l]
            max_sum = max(max_sum, prefix_sum[l] + mid_sum + prefix_sum[-1] - prefix_sum[r + 1])
            l -= 1
            r += 1
    return max_sum


n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

r = solve(n, a, b)
print(r)
