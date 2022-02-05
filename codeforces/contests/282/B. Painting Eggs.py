# https://codeforces.com/problemset/problem/282/B
# 23:10
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, eggs):
    # eggs = sorted(eggs, key=itemgetter(1))

    price_a = 0
    price_g = 0
    res = [None] * n
    for i in range(n):
        a, g = eggs[i]

        if abs(price_a + a - price_g) < abs(price_g + g - price_a):
            res[i] = 'A'
            price_a += a
        else:
            res[i] = 'G'
            price_g += g
    return ''.join(res)


if _DEBUG:
    assert solve(3, [(400, 600), (400, 600), (400, 600), ]) == 'AGA'

n = int(input())
eggs = [tuple(map(int, input().split())) for x in range(n)]
ans = solve(n, eggs)
sys.stdout.write(ans + '\n')
