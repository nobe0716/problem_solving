# https://codeforces.com/contest/1538/problem/D
import math

max_prime_limit = int(math.sqrt(10 ** 9)) + 1
prime_candidates = list(range(2, max_prime_limit + 1))
primes = set(prime_candidates)
for i in prime_candidates:
    if i not in primes:
        continue
    j = i * 2
    while j < max_prime_limit:
        primes.discard(j)
        j += i
primes = sorted(primes)
len_primes = len(primes)


def solve(a, b, k):
    if k == 0:
        return a == b
    elif k == 1:
        return a != b and (a % b == 0 or b % a == 0)

    def eval_n(x):
        c = 0
        for p in primes:
            if p ** 2 > x:
                break
            while x % p == 0:
                x //= p
                c += 1
        return c + (0 if x == 1 else 1)

    return eval_n(a) + eval_n(b) >= k


for _ in range(int(input())):
    a, b, k = map(int, input().split())
    r = solve(a, b, k)
    print('YES' if r else 'NO')
