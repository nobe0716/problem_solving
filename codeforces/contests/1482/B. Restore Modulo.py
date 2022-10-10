# 2022-10-09 23:33:41.490092
# https://codeforces.com/problemset/problem/1482/B
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


def proc(n, a):
    diffs = [a[i] - a[i - 1] for i in range(1, n)]
    # c == 0
    if all(e == 0 for e in diffs):
        return [0]
    elif any(e == 0 for e in diffs):
        return None
    if len(set(diffs)) == 1:
        return [0]
    # a[i + 1] == a[i] + c or a[i] + c - m
    # a[i + 1] - a[i] == c or (c - m)
    positive_diff = list(filter(lambda x: x > 0, diffs))
    negative_diff = list(filter(lambda x: x < 0, diffs))
    if len(set(positive_diff)) > 1 or len(set(negative_diff)) > 1:
        return None

    c = positive_diff[0]
    m = c - negative_diff[0]  # c - m == negative_diff

    if any(x >= m for x in a):
        return None
    return m, c


for _ in range(int(input())):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    ans = proc(n, a)

    if not ans:
        print('-1\n')
    else:
        print(' '.join(map(str, ans)) + '\n')
