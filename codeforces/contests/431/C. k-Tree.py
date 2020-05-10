import functools

_MODER = 1000000007


def solve(n, k, d):
    @functools.lru_cache(None)
    def find_not_yet_d(n):
        if n < d:
            return 0

        r = 0
        for i in range(1, min(n, k) + 1):
            if i >= d:
                r += find_used_d(n - i)
            else:
                r += find_not_yet_d(n - i)
        return r % _MODER

    @functools.lru_cache(None)
    def find_used_d(n):
        if n == 0:
            return 1
        r = 0
        for i in range(1, min(n, k) + 1):
            r += find_used_d(n - i)
        return r % _MODER

    return find_not_yet_d(n) % _MODER


n, k, d = map(int, input().split())
print(solve(n, k, d))
