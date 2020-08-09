from typing import List

_MAX_N = 10 ** 5
prefix_sum = [0] * _MAX_N
prefix_max = [0] * _MAX_N


def solve(n: int, k: int, z: int, a: List[int]):
    global prefix_sum, prefix_max

    prefix_sum[0] = a[0]
    prefix_max[1] = a[0] + a[1]
    for i in range(1, k + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i]
    for i in range(2, k + 1):
        prefix_max[i] = max(prefix_max[i - 1], a[i - 1] + a[i])

    max_val = prefix_sum[k]
    for i in range(1, z + 1):
        max_candidate = prefix_sum[k - 2 * i] + i * prefix_max[k - 2 * i + 1]
        max_val = max(max_val, max_candidate)
    return max_val


# assert solve(18, 11, 4, [11, 19, 18, 19, 19, 5, 14, 15, 17, 4, 10, 9, 8, 17, 9, 2, 15, 10]) == 219
# assert solve(5, 4, 0, [1, 5, 4, 3, 2]) == 15
# assert solve(5, 4, 1, [1, 5, 4, 3, 2]) == 19
# assert solve(5, 4, 4, [10, 20, 30, 40, 50]) == 150
# assert solve(10, 7, 3, [4, 6, 8, 2, 9, 9, 7, 4, 10, 9]) == 56

for _ in range(int(input())):
    n, k, z = map(int, input().split())
    a = list(map(int, input().split()))
    r = solve(n, k, z, a)
    print(r)
