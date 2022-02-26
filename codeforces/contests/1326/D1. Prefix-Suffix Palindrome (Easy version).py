# 2022-02-13 21:04:05.991615
# https://codeforces.com/problemset/problem/1326/D1
import sys

_DEBUG = True
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


def solve(s):
    def is_palindromic(lo, hi):
        while lo < hi and s[lo] == s[hi]:
            lo += 1
            hi -= 1
        return lo >= hi

    n = len(s)
    if is_palindromic(0, n - 1):
        return s[::-1]

    prefix_bound, suffix_bound = 0, n - 1
    while prefix_bound < suffix_bound and s[prefix_bound] == s[suffix_bound]:
        prefix_bound, suffix_bound = prefix_bound + 1, suffix_bound - 1

    lv = 1
    ls = s[0]
    for i in range(suffix_bound + 1):
        if i < prefix_bound:
            if (i + 1) * 2 > lv:
                lv = (i + 1) * 2
                ls = s[:i + 1] + s[-i - 2:]
        else:
            if is_palindromic(prefix_bound, i) and i + prefix_bound + 1 > lv:
                lv = i + prefix_bound + 1
                ls = s[:i + 1] + s[suffix_bound + 1:]

    for i in range(n - 1, prefix_bound - 1, -1):
        if i > suffix_bound:
            if (n - i) * 2 > lv:
                lv = (n - i) * 2
                ls = s[:n - i] + s[i:]
        else:
            if is_palindromic(i, suffix_bound) and prefix_bound + n - i > lv:
                lv = prefix_bound + n - i
                ls = s[:prefix_bound] + s[i:]

    if _DEBUG:
        print(ls)
    return ls


assert solve('yvaamavy') == 'yvaaavy'

if _DEBUG:
    assert solve('abcdfdcecba') == 'abcdfdcba'  # i == 5 j == 9
    assert solve('acbba') == 'abba'
    assert solve('abbca') == 'abba'
    assert solve('a') == 'a'
    assert solve('abbaxyzyx') == 'xyzyx'

for _ in range(int(input())):
    s = input().strip()
    ans = solve(s)

    if _DEBUG:
        print(ans)
    else:
        print(ans + '\n')
