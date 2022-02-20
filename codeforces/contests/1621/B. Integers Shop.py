# 2022-02-20 14:44:05.038473
# https://codeforces.com/problemset/problem/1621/B
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


def proc(n, a):
    lo_index = 0
    hi_index = 0
    longest_index = 0

    ans = [a[0][2]]

    for i in range(1, n):
        l, r, c = a[i]

        if l < a[lo_index][0] or (l == a[lo_index][0] and c < a[lo_index][2]):
            lo_index = i
        if r > a[hi_index][1] or (r == a[hi_index][1] and c < a[hi_index][2]):
            hi_index = i
        if r - l > (a[longest_index][1] - a[longest_index][0]) or (r - l == a[longest_index][1] - a[longest_index][0] and c < a[longest_index][2]):
            longest_index = i

        min_cost = sum(a[j][2] for j in {lo_index, hi_index})
        if a[longest_index][0] == a[lo_index][0] and a[longest_index][1] == a[hi_index][1]:
            min_cost = min(min_cost, a[longest_index][2])

        ans.append(min_cost)
    return ans


for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        l, r, c = map(int, input().split())
        a.append((l, r, c))
    ans = proc(n, a)
    if _DEBUG:
        print('\n'.join(map(str, ans)))
    else:
        print('\n'.join(map(str, ans)) + '\n')
