import bisect
import math

_THRESHOLD = 10 ** 6

prime_set = set(range(2, _THRESHOLD))
for i in range(2, int(math.sqrt(_THRESHOLD))):
    if i not in prime_set:
        continue
    for j in range(2 * i, _THRESHOLD, i):
        prime_set.discard(j)
sorted_primes = sorted(prime_set)


def solve(n):
    for i in range(1, 100000):
        if i in prime_set:
            continue

        m = [[i] * n for _ in range(n)]
        if sum(m[0]) in prime_set:
            return m

        idx = bisect.bisect(sorted_primes, i * (n - 1))
        target_prime = sorted_primes[idx]
        v = target_prime - (n - 1) * i
        if v in prime_set:
            continue
        for i in range(n):
            m[i][n - 1] = m[n - 1][i] = v

        idx = bisect.bisect(sorted_primes, v * (n - 1))
        target_prime = sorted_primes[idx]
        v = target_prime - (n - 1) * v

        if v in prime_set:
            continue
        m[n - 1][n - 1] = v
        return m
    return None


for _ in range(int(input())):
    n = int(input())
    m = solve(n)
    print('\n'.join(' '.join(map(str, _)) for _ in m))
