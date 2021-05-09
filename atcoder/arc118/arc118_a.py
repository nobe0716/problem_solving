import math

_DEBUG = True


def solve(t, n):
    def get_price(a):
        return int(math.floor((100 + t) * a / 100))

    num_set = set()
    for i in range(1, 10001):
        num_set.add(get_price(i))

    candidates = []

    for i in range(1, 10000 + t * 100):
        if i in num_set:
            continue
        candidates.append(i)

    n -= 1
    res = int(10000 + t * 100) * (n // len(candidates)) + candidates[n % len(candidates)]
    return res


if _DEBUG:
    assert solve(3, 1) == 34
    assert solve(3, 2) == 68
    assert solve(3, 3) == 102
    assert solve(3, 4) == 137
    assert solve(3, 5) == 171
    assert solve(1, 1000000000) == 100999999999
    assert solve(10, 1) == 10
    assert solve(20, 1) == 5
    assert solve(20, 2) == 11
    assert solve(20, 3) == 17

t, n = map(int, input().split())
print(solve(t, n))
