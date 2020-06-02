import sys

sys.setrecursionlimit(100000)


def solve(v, a):
    min_value = min(a)

    def rec(v):
        if v == 0 or v < min_value:
            return ''
        a.sort(key=lambda x: ((v - x[1]) // min_value, x[0]), reverse=True)
        number, price = a[0]
        if price == min_value:
            return str(number) * (v // price) + rec(v % price)
        optimal_digits = (v - price) // min_value + 1
        i = (v - min_value * optimal_digits) // (price - min_value)
        return str(number) * i + rec(v - i * price)

    a = list(enumerate([10 ** 7] + a))
    return rec(v)


# assert solve(5, list(map(int, '5 4 3 2 1 2 3 4 5'.split()))) == '55555'

v = int(input())
a = list(map(int, input().split()))

r = solve(v, a)
if not r or r == '':
    print(-1)
else:
    print(r)
