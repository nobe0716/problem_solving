# 2022-08-27 17:37:30.973256
# https://codeforces.com/problemset/problem/1603/B
import random
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write

"""
x >= y
    n = x + y
    
    (x + y) % x = y (since y < x)
    y % n = y (since n > y)
x < y
    y % n -> y if y < n but n % x is lte x so n should be less than y
    n = y - (y % x) // 2
    
    suppose y = ax + b (0<=b<x, n = ax + b//2)
        n % x = (ax + b//2) % x = b // 2
        y % n = (ax + b) % (ax + b // 2) == b // 2 
"""


def proc(x, y):
    if x > y:
        return x + y
    else:
        return y - (y % x) // 2


# while True:
#     x = random.randint(1, 10 ** 9 // 2) * 2
#     y = random.randint(1, 10 ** 9 // 2) * 2
#
#     n = proc(x, y)
#     print(x, y, n)
#     if n % x != y % n:
#         print('{} % {}({}) != {} % {}({})'.format(n, x, n % x, y, n, y % n))
#         exit(1)

for _ in range(int(input())):
    x, y = map(int, input().split())
    n = proc(x, y)
    print(n)

    # assert n % x == y % n
