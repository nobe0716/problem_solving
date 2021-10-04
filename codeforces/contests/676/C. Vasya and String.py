# https://codeforces.com/problemset/problem/676/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, k, s):
    an = bn = ans = i = 0

    for e in s:
        if e == 'a':
            an += 1
        else:
            bn += 1

        while min(an, bn) > k:
            if s[i] == 'a':
                an -= 1
            else:
                bn -= 1
            i += 1
        ans = max(an + bn, ans)

    return ans


assert solve(8, 1, 'aabaabaa') == 5
assert solve(1, 0, 'a') == 1
assert solve(4, 2, 'abba') == 4

n, k = map(int, input().split())
s = input()

ans = solve(n, k, s)
print(ans)
