import math
from functools import reduce


def lcm(a, b):
    g = math.gcd(a, b)
    return a // g * b // g * g


def solve(n):
    return max(find_from_n(n), find_from_n(n - 1))


def find_from_n(n):
    if n == 0:
        return 1
    a = [n]
    for i in range(n - 1, 0, -1):
        if len(a) >= 3:
            break
        if all(math.gcd(i, x) == 1 for x in a):
            a.append(i)
    if len(a) >= 3 and a[-1] == 1:
        a[-1] = a[1] - 1
    return reduce(lambda x, y: lcm(x, y), a, a[0])


n = int(input())
r = max(solve(n), solve(n - 1))
print(r)
