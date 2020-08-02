import sys
from collections import Counter

a, b = input(), input()

sys.setrecursionlimit(100)


def solve(a, b):
    def is_eq(l, a, b):
        if a == b:
            return True
        if l % 2 == 1:
            return a == b
        l //= 2
        a1, a2 = a[:l], a[l:]
        b1, b2 = b[:l], b[l:]
        return (is_eq(l, a1, b1) and is_eq(l, a2, b2)) or (is_eq(l, a1, b2) and is_eq(l, a2, b1))

    l = len(a)
    if Counter(a) != Counter(b):
        return False
    return is_eq(l, a, b)


print('YES' if solve(a, b) else 'NO')
