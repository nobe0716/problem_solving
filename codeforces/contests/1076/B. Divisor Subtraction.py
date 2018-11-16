import math

n = int(input())
l = int(math.sqrt(n)) + 1
is_prime = [True] * l

is_prime[0] = is_prime[1] = False
primes = []
for i in range(2, l):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * 2, l, i):
            is_prime[j] = False

c = 0
while n % 2 == 1:
    subtracted = False
    for p in primes:
        if n % p == 0:
            n -= p
            c += 1
            subtracted = True
            break
    if not subtracted:
        n = 0
        c += 1
print(c + (n // 2))
