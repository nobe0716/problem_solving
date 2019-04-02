# -*- coding:utf-8 -*-
"""
WIP

## Name of Prob
D. The Beatles

## Link
https://codeforces.com/contest/1143/problem/D

## Note
Sergey starts from s and moves by l

## Input
n, k
a, b

1 <= n, k <= 100,000
- n: num of restaurants
- k: distance per restaurants
0 <= a, b <= k // 2
- a: the distances to the nearest restaurants from the initial city
- b: the distances to the nearest restaurants from the city Sergey made the first stop at

## Output
x, y
x: minimum number of stops (excluding the first) Sergey could have done before returning to s.
y: y is the maximum number of stops (excluding the first) Sergey could have done before returning to s.

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
