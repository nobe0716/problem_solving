# 2022-02-13 19:32:32.612926
# https://codeforces.com/problemset/problem/1547/E
import sys

_DEBUG = False

if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


def solve(n, k, air_pos, air_tmp):
    conditioners = zip(air_pos, air_tmp)
    airs = []
    for pos, tmp in sorted(conditioners):
        while airs and airs[-1][1] > tmp + pos - airs[-1][0]:
            airs.pop()
        if not airs or airs[-1][1] + (pos - airs[-1][0]) > tmp:
            airs.append((pos, tmp))

    temperatures = [0] * (n + 1)
    j = 0
    for i in range(1, n + 1):
        temperatures[i] = airs[j][1] + abs(i - airs[j][0])
        if j < len(airs) - 1 and temperatures[i] >= airs[j + 1][1] + abs(i - airs[j + 1][0]):
            temperatures[i] = airs[j + 1][1] + abs(i - airs[j + 1][0])
            j += 1
    return temperatures[1:]


if _DEBUG:
    assert solve(6, 3, [6, 1, 3, ], [5, 5, 5, ]) == [5, 6, 5, 6, 6, 5, ]
    assert solve(6, 2, [2, 5, ], [14, 16, ], ) == [15, 14, 15, 16, 16, 17]

for _ in range(int(input())):
    dummy = input()
    n, k = map(int, input().split())
    air_pos = list(map(int, input().split()))
    air_tmp = list(map(int, input().split()))
    res = solve(n, k, air_pos, air_tmp)
    if _DEBUG:
        print(' '.join(map(str, res)))
    else:
        print(' '.join(map(str, res)) + '\n')
