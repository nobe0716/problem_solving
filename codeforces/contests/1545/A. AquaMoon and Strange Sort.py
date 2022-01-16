# https://codeforces.com/problemset/problem/1545/A
import sys
from collections import defaultdict

input = sys.stdin.readline


def solve(n, a):
    num_to_pos = defaultdict(lambda: [float('inf'), float('-inf')])
    for i, e in enumerate(sorted(a)):
        num_to_pos[e][0] = min(num_to_pos[e][0], i)
        num_to_pos[e][1] = max(num_to_pos[e][1], i)

    deltas = defaultdict(list)
    for i, e in enumerate(a):
        deltas[e].append(abs(i - num_to_pos[e][0]))
        num_to_pos[e][0] += 1

    for moves in deltas.values():
        if sum(moves) % 2 != 0:
            return False
        if sum(1 if e % 2 == 1 else 0 for e in moves) % 2 != 0:
            return False

        pos = []
        for i, e in enumerate(moves):
            if e % 2 == 1:
                pos.append(i)
                # if pos and i - pos[-1]

        odd_pos = 0
        even_pos = 0
        for e in pos:
            if e % 2 == 1:
                odd_pos += 1
            else:
                even_pos += 1
        if odd_pos != even_pos:
            return False
    return True


assert solve(98, list(int(x) for x in '89 30 30 89 68 78 14 68 72 68 89 39 30 72 14 30 68 30 68 14 30 68 68 68 39 14 14 14 68 68 30 72 68 30 10 72 42 14 89 39 30 72 78 89 68 39 30 14 39 39 14 68 39 42 30 68 39 30 72 68 39 30 78 72 68 39 14 68 68 72 72 14 68 30 14 68 72 68 39 89 14 14 68 30 68 89 72 68 89 14 72 68 68 98 72 39 30 78'.split()))
assert solve(6, list(int(x) for x in '2 1 2 1 2 1'.split())) is False
assert solve(8, list(int(x) for x in '1 3 1 1 4 5 4 4'.split()))

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(n, a)
    if ans:
        print('YES')
    else:
        print('NO')
