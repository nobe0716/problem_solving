# https://codeforces.com/problemset/problem/1552/B
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, athletes):
    def is_better(x, y):
        return sum(1 if a < b else 0 for a, b in zip(athletes[x], athletes[y])) >= 3

    winner = 0
    for i in range(1, n):
        if is_better(winner, i):
            continue
        else:
            winner = i

    for i in range(n):
        if i == winner:
            continue
        if not is_better(winner, i):
            return -1
    return winner + 1


for _ in range(int(input())):
    n = int(input())
    athletes = []
    for _ in range(n):
        athletes.append(list(map(int, input().strip().split())))

    ans = solve(n, athletes)
    print(ans)
