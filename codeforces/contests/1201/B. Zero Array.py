# https://codeforces.com/contest/1201/problem/B
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a):
    sum_of_a = sum(a)
    max_of_a = max(a)
    return 'YES' if sum_of_a % 2 == 0 and max_of_a <= sum_of_a // 2 else 'NO'


n = int(input())
a = [int(x) for x in input().strip().split()]
ans = solve(n, a)
print(ans)
