# https://codeforces.com/problemset/problem/1418/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline

table_me = [0] * (2 * 10 ** 5 + 1)
table_fr = [0] * (2 * 10 ** 5 + 1)


def solve(n, a):
    if n == 1:
        return a[0]
    for i in range(n):
        table_me[i] = float('inf')
        table_fr[i] = float('inf')

    table_fr[0] = a[0]
    table_fr[1] = a[0] + a[1]
    table_me[0] = float('inf')
    table_me[1] = a[0]

    for i in range(2, n):
        table_me[i] = min(table_fr[i - 1], table_fr[i - 2])
        table_fr[i] = min(table_me[i - 1] + a[i], table_me[i - 2] + a[i - 1] + a[i])

    return min(table_me[n - 1], table_fr[n - 1])


# assert solve(5, list(int(x) for x in '1 1 1 1 0'.split())) == 2
# assert solve(8, list(int(x) for x in '1 0 1 1 0 1 1 1'.split())) == 2
# assert solve(7, list(int(x) for x in '1 1 1 1 0 0 1'.split())) == 2
# assert solve(6, list(int(x) for x in '1 1 1 1 1 1'.split())) == 2

for _ in range(int(input())):
    n = int(input().strip())
    a = [int(x) for x in input().strip().split()]
    ans = solve(n, a)
    print(ans)
