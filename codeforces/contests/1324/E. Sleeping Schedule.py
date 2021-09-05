# https://codeforces.com/contest/1324/problem/E
import sys

input = sys.stdin.buffer.readline

n, h, l, r = map(int, input().split())
t = [[float('-inf')] * (n + 1) for _ in range(n + 1)]
t[0][0] = 0
a = [0] + [int(x) for x in input().split()]
acc_sleep_time = 0
for i in range(1, n + 1):
    acc_sleep_time += a[i]

    t[i][0] = t[i - 1][0]
    if l <= acc_sleep_time % h <= r:
        t[i][0] += 1

    for j in range(1, i + 1):
        t[i][j] = max(t[i][j], max(t[i - 1][j - 1], t[i - 1][j]) + (1 if l <= (acc_sleep_time - j) % h <= r else 0))
# print(t[n])
print(max(t[n]))
