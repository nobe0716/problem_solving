import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solve(n):
    if is_prime(n):
        return 1
    elif n % 2 == 0 or is_prime(n - 2):
        return 2
    return 3


n = int(input())

r = solve(n)
print(r)
