# 2022-02-20 13:50:32.280037
# https://codeforces.com/problemset/problem/460/B
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def proc(a, b, c):
    def calc_sx(x):
        r = 0
        while x > 0:
            r += x % 10
            x //= 10
        return r

    res = []
    for sx in range(1, 82):
        x = b * sx ** a + c
        if x > 10 ** 9:
            continue
        if calc_sx(x) == sx:
            res.append(x)
    return res


a, b, c = map(int, input().split())
ans = proc(a, b, c)
print(len(ans))
print(' '.join(map(str, ans)))
