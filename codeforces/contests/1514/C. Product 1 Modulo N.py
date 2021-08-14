# https://codeforces.com/contest/1514/problem/C


def get_mod(n, r):
    c = 1
    for e in r:
        c = (c * e) % n
    return c


def solve(n):
    def factorize(n):
        v = []
        p = 2
        while n > 1:
            if n % p == 0:
                v.append(p)
                while n % p == 0:
                    n //= p
            p += 1
        return v

    v = set(range(1, n))
    factors = factorize(n)

    for i in range(2, n):
        if any(i % x == 0 for x in factors):
            v.discard(i)

    r = sorted(v)

    while True:
        m = get_mod(n, r)
        if m == 1:
            break
        r.remove(m)

    return r


# for i in range(2, 10 ** 5 + 1):
#     r = solve(i)
#     assert 1 == get_mod(i, r)
#     print(i)

n = int(input())
r = solve(n)
print(len(r))
print(' '.join(str(x) for x in r))
