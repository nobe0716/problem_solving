import math

_MOD = 10 ** 9 + 7


def solve(n: int, m: int) -> int:
    return math.factorial(n + 2 * m - 1) // math.factorial(2 * m) // math.factorial(n - 1) % _MOD

assert solve(2, 2) == 5
assert solve(10, 1) == 55
assert solve(723, 9) == 157557417

n, m = map(int, input().split())
r = solve(n, m)
print(r)
