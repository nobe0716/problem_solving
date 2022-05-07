# 2022-05-07T23:05:54.301Z
import math
import sys
from collections import Counter

input = sys.stdin.readline


def proc(a_list, b_list):
    base = 0
    c = Counter()
    for a, b in zip(a_list, b_list):
        if a == 0 and b == 0:
            base += 1
        elif a == 0 and b != 0:
            continue
        else:
            g = math.gcd(b, a)
            a //= g
            b //= g
            # d = -b/a
            if a <= 0 and b >= 0:
                a, b = -a, -b
            elif a <= 0 and b <= 0:
                a, b = -a, -b
            c[(a, b)] += 1

    cn = (c.most_common(1)[0][1] if c else 0)
    return base + cn


n = int(input())
a_list = list(map(int, input().strip().split()))
b_list = list(map(int, input().strip().split()))

print(proc(a_list, b_list))
