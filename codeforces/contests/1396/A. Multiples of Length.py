# https://codeforces.com/contest/1396/problem/A
import sys

input = sys.stdin.readline
n = int(input())
a = [int(x) for x in input().strip().split()]

if n == 1:
    print('1 1\n{}\n1 1\n0\n1 1\n0'.format(-a[0]))
else:
    print(1, 1)
    print(-a[0])
    print(1, n)
    print(' '.join(map(str, [0] + [-n * x for x in a[1:]])))
    print(2, n)
    print(' '.join(str((n - 1) * x) for x in a[1:]))
