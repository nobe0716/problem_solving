# https://codeforces.com/problemset/problem/1537/D
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.buffer.readline


def solve(n):
    if n % 2 == 1:
        return 'Bob'
    cnt = 0
    while n % 2 == 0:
        n //= 2
        cnt += 1

    if n > 1 or cnt % 2 == 0:
        return 'Alice'
    return 'Bob'


for _ in range(int(input())):
    n = int(input())
    ans = solve(n)
    print(ans)
