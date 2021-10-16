# https://codeforces.com/problemset/problem/1301/B
import sys

_MAX_VAL = float('inf')

_MIN_VAL = float('-inf')

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a):
    min_neighbor = _MAX_VAL
    max_neighbor = _MIN_VAL

    maximum_diff = _MIN_VAL
    for i in range(1, n):
        if a[i] != -1 and a[i - 1] != -1:
            maximum_diff = max(maximum_diff, abs(a[i] - a[i - 1]))
        elif a[i] == -1 and a[i - 1] == -1:
            continue
        elif a[i] == -1:
            min_neighbor = min(min_neighbor, a[i - 1])
            max_neighbor = max(max_neighbor, a[i - 1])
        elif a[i - 1] == -1:
            min_neighbor = min(min_neighbor, a[i])
            max_neighbor = max(max_neighbor, a[i])

    if min_neighbor == _MAX_VAL and max_neighbor == _MIN_VAL and maximum_diff == _MIN_VAL:
        return 0, 42

    m = k = 0
    if maximum_diff != _MIN_VAL:
        m = maximum_diff
        k = 42

    if min_neighbor != _MAX_VAL:
        k = (min_neighbor + max_neighbor) // 2
        m_candidate = max(abs(min_neighbor - k), abs(max_neighbor - k))
        if m_candidate > m:
            m = m_candidate
    return m, k


assert solve(6, [1, -1, -1, 2, 2, -1]) == (1, 1)
assert solve(6, [-1, -1, 9, -1, 3, -1]) == (3, 6)
assert solve(2, [-1, -1]) == (0, 42)

for _ in range(int(input())):
    n = int(input().strip())
    a = [int(x) for x in input().strip().split()]

    m, k = solve(n, a)
    print(m, k)
