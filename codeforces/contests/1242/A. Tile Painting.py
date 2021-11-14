# https://codeforces.com/contest/1242/problem/A
import math

_DEBUG = True
_DEBUG = False


def solve(n: int) -> int:
    for i in range(2, int(math.floor(math.sqrt(n))) + 1):
        if n % i != 0:
            continue
        while n > 1 and n % i == 0:
            n /= i
        if n == 1:
            return i
        return 1
    return n


if _DEBUG:
    assert solve(951069502319) == 1
    assert solve(1) == 1
    assert solve(2) == 2
    assert solve(3) == 3
    assert solve(6) == 1
    assert solve(7) == 7
    assert solve(8) == 2
    assert solve(9) == 3
    assert solve(1000000000000) == 1
    assert solve(963201794869) == 963201794869
    assert solve(902076349729) == 949777
    assert solve(549755813888) == 2
    assert solve(951069502319) == 1
n = int(input())
print(solve(n))
