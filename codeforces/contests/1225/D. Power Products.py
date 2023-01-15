# 2023-01-16 00:02:19.026780
# https://codeforces.com/contest/1225/problem/D
from collections import Counter


def proc(n, k, a):
    def factorize(n):
        i = 2
        c = Counter()
        while i ** 2 <= n:
            while n % i == 0:
                c[i] = (c[i] + 1) % k
                n //= i
                if c[i] == 0:
                    del c[i]
            i += 1

        if n > 1:
            c[n] += 1
        return c

    factors = []

    zero_count = 0
    for i, e in enumerate(a):
        factorized = factorize(e)
        if len(factorized) == 0 or all(v == 0 for v in factorized.values()):
            zero_count += 1
            continue
        factors.append(factorized)

    accumulator = Counter()
    for factorized in factors:
        comp_key = tuple((key, value) for key, value in sorted(factorized.items()))
        accumulator[comp_key] += 1

    res = 0
    for factorized in factors:
        comp_key = tuple((key, k - value) for key, value in sorted(factorized.items()))
        if k % 2 == 0 and all(v == k // 2 for v in factorized.values()):
            res += (accumulator[comp_key] - 1)
        else:
            res += accumulator[comp_key]

    res //= 2
    if zero_count > 0:
        res += zero_count * (zero_count - 1) // 2
    return res


assert proc(6, 3, [1, 3, 9, 8, 24, 1]) == 5
assert proc(10, 2, [7, 4, 10, 9, 2, 8, 8, 7, 3, 7]) == 7
assert proc(2, 2, [40, 90]) == 1

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(proc(n, k, a))
