# 2022-03-05 19:35:51.801997
# https://codeforces.com/problemset/problem/743/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n):
    if n == 1:
        return [-1]
    z = n

    while z < 10 ** 9:
        if z % 2 == 1:
            z += n
            continue

        target_sum = 2 * z // n - 1

        for i in range(2, target_sum // 2 + 1):
            if z % i != 0:
                continue
            if z % (target_sum - i) != 0:
                continue
            x = z // (target_sum - i)
            y = z // i
            return x, y, z
        z += n
    return [-1]


n = int(input())

ans = proc(n)
print(' '.join(map(str, ans)))
