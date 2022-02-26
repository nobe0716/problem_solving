# 2022-02-27 01:07:46.034979
# https://codeforces.com/problemset/problem/1416/A
import sys
from collections import defaultdict

_DEBUG = True
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


def proc(n, a):
    num_pos = defaultdict(list)
    num_gaps = defaultdict(int)

    gap_to_min = {}
    for i, e in enumerate(a):
        num_pos[e].append(i)

    for k in num_pos:
        num_gaps[k] = num_pos[k][0] + 1
        for i in range(1, len(num_pos[k])):
            num_gaps[k] = max(num_gaps[k], num_pos[k][i] - num_pos[k][i - 1])
        num_gaps[k] = max(num_gaps[k], n - num_pos[k][-1])

        if num_gaps[k] not in gap_to_min:
            gap_to_min[num_gaps[k]] = k
        else:
            gap_to_min[num_gaps[k]] = min(gap_to_min[num_gaps[k]], k)

    t = [float('inf')] * n
    t[0] = gap_to_min[1] if 1 in gap_to_min else -1
    for i in range(1, n):
        t[i] = gap_to_min[i + 1] if i + 1 in gap_to_min else -1
        if t[i - 1] != -1 and (t[i] == -1 or t[i] > t[i - 1]):
            t[i] = t[i - 1]
    return t


if _DEBUG:
    assert proc(6, [1, 3, 1, 5, 3, 1]) == [-1, -1, 1, 1, 1, 1]
    assert proc(5, [4, 4, 4, 4, 2]) == [-1, 4, 4, 4, 2]

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if _DEBUG:
        print(' '.join(map(str, proc(n, a))))
    else:
        print(' '.join(map(str, proc(n, a))) + '\n')
