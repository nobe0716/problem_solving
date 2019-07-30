_MODER = 998244353


def solve(n, a):
    r = 0
    for e in a:
        ns = ''
        for ch in str(e):
            ns += (ch + ch)
        r = (r + (int(ns) * n % _MODER)) % _MODER
    return r


n = int(input())
a = list(map(int, input().split()))

r = solve(n, a)
print(r)
