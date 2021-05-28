# https://codeforces.com/contest/1409/problem/D
import math


def solve(t, s) -> int:
    def get_sum_digits(v):
        current_sum = 0
        while v > 0:
            current_sum += v % 10
            v //= 10
        return current_sum

    if get_sum_digits(t) <= s:
        return 0

    base = 10
    for _ in range(math.ceil(math.log10(t)) + 1):
        new_t = t + (base - t % base)
        if get_sum_digits(new_t) <= s:
            return new_t - t
        base *= 10

    return None


# assert solve(100000000000000001, 1) == 899999999999999999
# assert solve(99, 1) == 1
# assert solve(217871987498122, 10) == 2128012501878
# assert solve(500, 4) == 500
# assert solve(2, 1) == 8
# assert solve(1, 1) == 0

for _ in range(int(input())):
    t, s = map(int, input().split())
    r = solve(t, s)

    print(r)
