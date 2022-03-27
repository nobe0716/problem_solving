# 2022-03-27 20:22:49.198601
# https://codeforces.com/problemset/problem/702/B
import sys
from collections import Counter

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write

n = int(input())
a = list(map(int, input().split()))


def proc(n, a):
    c = Counter(a)

    pow_of_two = [2 ** i for i in range(33) if 2 ** i <= 2 * 10 ** 9]

    ans = 0
    for k, v in c.items():
        for x in pow_of_two:
            if x <= k:
                continue

            if (x - k) not in c or k > x - k:
                continue

            if x == 2 * k:
                ans += v * (v - 1) // 2
            else:
                ans += v * c[x - k]
    return ans


ans = proc(n, a)
print(ans)
