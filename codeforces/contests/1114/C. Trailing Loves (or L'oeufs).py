import math
from collections import defaultdict


def get_primes(upper_bound):
    p = set(range(2, upper_bound + 1))
    for i in range(2, upper_bound + 1):
        if i not in p:
            continue
        for j in range(i * 2, upper_bound + 1, i):
            if j in p:
                p.remove(j)
    return p


def prime_factorization(v, prime_set):
    r = defaultdict(int)
    for p in prime_set:
        while v > 0 and v % p == 0:
            r[p] += 1
            v //= p
    if v > 1:
        r[v] = 1
    return r


def get_count(n, p):
    r = 0
    v = p
    while n >= v:
        r += n // v
        v *= p
    return r


n, b = map(int, input().split())

primes = get_primes(int(math.sqrt(b)) + 1)
factorized_n = prime_factorization(b, primes)
v = float('inf')

for prime_num, prime_count in factorized_n.items():  # (k**v)
    n_has_count = get_count(n, prime_num)
    v = min(v, n_has_count // prime_count)

print(v)
