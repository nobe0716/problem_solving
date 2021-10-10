# https://codeforces.com/problemset/problem/1538/F
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(l: int, r: int) -> int:
    def count_changes(v: int) -> int:
        base = 1
        count = 0
        while v > 0:
            count += base * (v % 10)
            base = base * 10 + 1
            v //= 10
        return count

    return count_changes(r) - count_changes(l)


assert solve(9, 10) == 2
assert solve(10, 20) == 11
assert solve(1, 9) == 8
assert solve(1, 1000000000) == 1111111110

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(solve(l, r))
