# https://codeforces.com/problemset/problem/1340/A
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a):
    d = {a[i]: i for i in range(n)}
    v = 1
    hi = n
    while v <= n:
        i = d[v]
        tmp = i
        while i < hi:
            if a[i] != v:
                return False
            i += 1
            v += 1
        hi = tmp
    return True


for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    ans = solve(n, a)
    print('YES' if ans else 'NO')
