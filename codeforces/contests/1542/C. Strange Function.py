# 2022-02-26 15:33:52.959134
# https://codeforces.com/problemset/problem/1542/C
import math
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline

_MODULO = 10 ** 9 + 7
"""

t(i) = number of elements(x) that f(x) == i

num of elements of lcm(1 ... (i - 1)) - num of elements of lcm(1 ... (i))
"""


def proc(n):
    def lcm(a, b):
        g = math.gcd(a, b)
        return a // g * b

    old_lcm = 1
    sum_of_values = 0
    for i in range(2, 42):
        new_lcm = lcm(old_lcm, i)
        ti = n // old_lcm - n // new_lcm

        old_lcm = new_lcm
        sum_of_values = (sum_of_values + ti * i) % _MODULO
    return sum_of_values


for _ in range(int(input())):
    n = int(input())
    ans = proc(n)
    print(ans)
