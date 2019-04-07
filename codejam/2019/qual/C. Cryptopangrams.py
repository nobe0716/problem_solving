"""
## Name of Prob
Cryptopangrams

## Link
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b

## Note

crypto algorithm
- select 26 prime number increasing order
- remove spaces, upper to plain text, encode to prime numbers
- product two primes pair from i to n - 1

## Input
n; upper bound of chosen prime number (N >= 101)
l; length of ciphertext

## Output
s; (l + 1) len upper case text

## Strategy

consider given str as

p_head*p_0 p_0*p_1 p_1*p_2 , ... p_(n-2)*p_(n-1) p_(n-1)*p_tail

first approach
```
find two prime for first token (p_first, p_second)
determine which one should be p_head by calculating s[1] % p_first and s[1] % p_second
iterate s and generate p_i
add p_i, p_head and p_tail to set and sort to find prime-alphabet mapping
```

now

1. find two different incident words, which are a[i] and a[i + 1]
2. get gcd of two number, it will be pivot prime
3. divide a[i-1 ... 0] and a[i+1 ... l - 1] to construct list of prime
4. prime-alphabet mapping will be easily made by sorting set of primes
5. decode primes using dictionary described above.

"""
from collections import deque


def get_gcd(a, b):
    if a < b:
        return get_gcd(b, a)
    if a % b == 0:
        return b
    return get_gcd(b, a % b)


for t in range(int(input())):
    n, l = map(int, input().split())
    nums = list(map(int, input().split()))

    i = 0
    while nums[i] == nums[i + 1]:
        i += 1
    pivot = i
    gcd = get_gcd(nums[i], nums[i + 1])
    primes = deque([gcd])

    prime = gcd
    for i in range(pivot, -1, -1):
        primes.appendleft(nums[i] // prime)
        prime = primes[0]
    prime = gcd
    for i in range(pivot + 1, l):
        primes.append(nums[i] // prime)
        prime = primes[-1]

    dict_prime_alphabet = {p: chr(ord('A') + i) for i, p in enumerate(sorted(set(primes)))}
    alphabets = list(map(lambda x: dict_prime_alphabet[x], primes))
    print("Case #{}: {}".format(t + 1, ''.join(alphabets)))
