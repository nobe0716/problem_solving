# https://codeforces.com/contest/1582/problem/A
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(a, b, c):
    c %= 2

    if c == 1:
        if a == 0 and b == 0:
            return 3
        elif a == 0:
            return 1
        elif b == 0:
            if a == 1:
                return 2
            elif a == 2:
                return 1
            else:
                a -= 3
                return 1 if a % 2 == 1 else 0
        else:
            a -= 1
            b -= 1
            return 1 if (a + 2 * b) % 2 == 1 else 0
    else:
        return 1 if (a + 2 * b) % 2 == 1 else 0


for _ in range(int(input())):
    a, b, c = map(int, input().strip().split())
    print(solve(a, b, c))
