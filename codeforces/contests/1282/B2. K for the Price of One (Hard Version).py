# 2022-05-14T22:43:15.690Z

import sys

input = sys.stdin.readline


def proc(n, p, k, a):
    def find(basis):
        for i in range(min(basis + k - 1, n), min(-1, basis - 1), -1):
            if prefix_sum[i] + mod_sum[i % k] <= p:
                return i
        return None

    a = sorted(a)
    prefix_sum = [0] * (n + 1)
    mod_sum = [0] + a[:k]

    for i in range(1, k):
        mod_sum[i] += mod_sum[i - 1]

    for i in range(k, n + 1):
        prefix_sum[i] += a[i - 1]
        prefix_sum[i] += prefix_sum[i - k]

    lo = 0
    hi = n
    ans = 0

    while lo <= hi:
        mid = (lo + hi) // 2

        found = find(mid)
        if found:
            ans = found
            lo = (mid + k)
        else:
            hi = mid - k
    return ans


assert proc(5, 6, 2, list(map(int, '2 4 3 5 7'.split()))) == 3
# assert proc(4, 6, 4, [3, 2, 3, 2]) == 4
# assert proc(5, 2, 3, [10, 1, 3, 9, 2]) == 1

for _ in range(int(input())):
    n, p, k = map(int, input().split())
    a = list(map(int, input().strip().split()))

    ans = proc(n, p, k, a)
    print(ans)
