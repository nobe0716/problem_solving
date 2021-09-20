# https://codeforces.com/contest/1513/problem/C
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.buffer.readline

_MOD = 10 ** 9 + 7
t = [0] * 200005
for i in range(9):
    t[i] = 2
t[9] = 3
for i in range(10, 200001):
    t[i] = (t[i - 9] + t[i - 10]) % _MOD
current_max = 9


def solve(n, m):
    global _MOD
    ans = 0
    while n > 0:
        if m - (10 - n % 10) < 0:
            ans += 1
        else:
            ans += t[m - (10 - n % 10)]
        ans %= _MOD
        n //= 10
    return ans % _MOD


# assert solve(1912, 1) == 5
# assert solve(12, 100) == 2115

for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = solve(n, m)
    print(ans)
