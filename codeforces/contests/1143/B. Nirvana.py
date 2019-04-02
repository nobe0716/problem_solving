# -*- coding:utf-8 -*-
"""
## Name of Prob
B. Nirvana

## Link
https://codeforces.com/contest/1143/problem/B

## Note
make multiple 9 as possible in [n-1, n] of digits

## Input
n; boundary

## Output
find maximum product of digits

## Strategy

decrease i-th digit by 1 and make i+1...l digit as 9
"""


def get_product(n):
    product = 1
    while n > 0 and product > 0:
        product *= (n % 10)
        n //= 10
    return product


n = input()
l = len(n)
n = int(n)
maximum_product = get_product(n)
for i in range(0, l):
    base = 10 ** (l - i - 1)
    v = (n // base - 1) * base + (base - 1)
    maximum_product = max(maximum_product, get_product(v))
print(maximum_product)
