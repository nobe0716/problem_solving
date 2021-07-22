import sys

input = sys.stdin.readline

n = int(input().strip())
a = [int(x) for x in input().strip().split()]

limit_prime = max(a)
primes = set(range(limit_prime + 1))
primes.discard(0)
primes.discard(1)

for e in list(primes):
    if e not in primes:
        continue
    v = e * 2
    while v <= limit_prime:
        primes.discard(v)
        v += e

r = 1
for prime in primes:
    second_smallest = smallest = float('inf')
    for e in a:
        c = 0
        while e % prime == 0:
            c += 1
            e //= prime

        if c < smallest:
            second_smallest = smallest
            smallest = c

            if second_smallest == 0:
                break
        elif c < second_smallest:
            second_smallest = c

            if second_smallest == 0:
                break

    if second_smallest > 0:
        # print(prime, second_smallest)
        r *= prime ** second_smallest

print(r)
