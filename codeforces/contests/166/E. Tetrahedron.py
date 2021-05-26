# https://codeforces.com/contest/166/problem/E

def solve(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 3
    _MODER = 10 ** 9 + 7

    a = 1
    b = 0
    for _ in range(n - 2):
        na = (2 * a + 3 * b)
        na %= _MODER
        a, b = na, a

    return (3 * a) % _MODER


assert solve(2) == 3
assert solve(4) == 21
assert solve(8) == 1641
assert solve(9) == 4920
assert solve(10) == 14763
assert solve(15) == 3587226
assert solve(30) == 782663359

n = int(input())
res = solve(n)
print(res)
