# 2022-02-13 20:27:53.266694
# https://codeforces.com/problemset/problem/1444/A
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(p, q):
    if p % q != 0:
        return p

    def factorization(x):
        factors = {}
        base = 2
        while base ** 2 <= x:
            c = 0
            while x % base == 0:
                x //= base
                c += 1
            if c > 0:
                factors[base] = c
            base += 1

        if x != 1:
            factors[x] = 1
        return factors

    def get_fp(x, b):
        c = 0
        while x % b == 0:
            x //= b
            c += 1
        return c

    fq = factorization(q)

    mv = float('inf')
    for k, v in fq.items():
        mv = min(mv, k ** (get_fp(p, k) - (v - 1)))

    ans = p // mv
    return ans if ans % q != 0 else 1


if _DEBUG:
    assert solve(1244094302301841, 35271721) == 5939

    assert solve(12, 6) == 4
    assert solve(10, 4) == 10
    assert solve(179, 822) == 179

for _ in range(int(input())):
    p, q = map(int, input().split())
    ans = solve(p, q)
    print(ans)
