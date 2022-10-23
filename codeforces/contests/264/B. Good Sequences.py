# 2022-10-23 20:09:01.339074
# https://codeforces.com/problemset/problem/264/B
import sys
from collections import defaultdict

_DEBUG = False
# _DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, a):
    prime_set = set(range(2, 10 ** 5))
    for e in range(2, 317):
        if e not in prime_set:
            continue
        for j in range(e * 2, 10 ** 5, e):
            prime_set.discard(j)
    prime_list = sorted(prime_set)

    def factorize(x):
        res = []
        for p in prime_list:
            if p > x:
                break
            if x % p != 0:
                continue
            res.append(p)
            while x % p == 0:
                x //= p
            if x in prime_set:
                res.append(x)
                break
        return res

    t = defaultdict(int)
    for e in a:
        factors = factorize(e)
        new_val = (max(t[f] for f in factors) if factors else 0) + 1

        for f in factors:
            t[f] = new_val

    return max(t.values()) if t else 1


n = int(input())
a = list(map(int, input().split()))

ans = proc(n, a)
print(ans)
