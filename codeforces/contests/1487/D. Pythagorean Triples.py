# https://codeforces.com/problemset/problem/1487/D
import math
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input().strip())
    ans = (int(math.floor(math.sqrt(2 * n - 1))) + 1) // 2 - 1
    print(ans)
