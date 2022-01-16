# https://codeforces.com/problemset/problem/1299/A
import sys

_BOUND = 32

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a):
    total_counter = [0] * _BOUND
    counters = []
    for e in a:
        binary = bin(e)[1:]
        lc = [0] * _BOUND
        for i, v in enumerate(binary[::-1]):
            if v == '1':
                lc[i] = 1
                total_counter[i] += 1
        counters.append(lc)

    max_v = 0
    max_i = 0
    for i in range(n):
        lc = counters[i]
        lv = 0
        for j, v in enumerate(lc):
            if total_counter[j] == 1 and lc[j] == 1:
                lv += 2 ** j

        if lv > max_v:
            max_i = i
            max_v = lv

    r = [a[max_i]]
    for i in range(n):
        if i == max_i:
            continue
        r.append(a[i])
    return ' '.join(map(str, r))


n = int(input())
a = [int(x) for x in input().strip().split()]

ans = solve(n, a)
print(ans)
