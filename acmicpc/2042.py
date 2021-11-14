import math
import sys

sys.setrecursionlimit(1000)
n, m, k = map(int, input().split())

a = []
for _ in range(n):
    a.append(int(input().strip()))
BASE = 2 ** int(math.ceil(math.log2(n)))
prefix_sum = [0] * (BASE + n)


def update_sum(b, delta):
    while b > 0:
        prefix_sum[b] += delta
        b //= 2


def get_sub_sum(b, c):
    if b == c:
        return prefix_sum[b]
    if b > c:
        return 0

    v = 0
    if c % 2 == 0:
        v += prefix_sum[c]
        c = (c - 1) // 2
    else:
        c //= 2

    if b % 2 == 1:
        v += prefix_sum[b]
        b = (b + 1) // 2
    else:
        b //= 2
    return v + get_sub_sum(b, c)


for i in range(BASE, BASE + n):
    update_sum(i, a[i - BASE])

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        b += BASE - 1
        update_sum(b, c - prefix_sum[b])
        # prefix_sum[b] = c
    else:
        print(get_sub_sum(BASE + b - 1, BASE + c - 1))
