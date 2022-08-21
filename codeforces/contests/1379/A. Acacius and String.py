# 2022-08-21 20:34:30.865519
# https://codeforces.com/problemset/problem/1379/A
import sys
from collections import defaultdict

PATTERN = 'abacaba'

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, s):
    def feasible(i):
        substitution = defaultdict(lambda: 'z')
        for j in range(7):
            if s[i + j] == PATTERN[j]:
                continue
            elif s[i + j] == '?':
                substitution[i + j] = PATTERN[j]
            else:
                return None
        if not substitution:
            return None

        c = 0
        for j in range(max(substitution.keys()) + 1):
            matches = True
            for k in range(7):
                if j + k >= n:
                    matches = False
                    break
                if (substitution[j + k] if s[j + k] == '?' else s[j + k]) != PATTERN[k]:
                    matches = False
                    break

            if matches:
                c += 1
        return substitution if c == 1 else None

    c = 0
    for i in range(n - 6):  # len('abacaba') == 7
        if s[i:i + 7] == PATTERN:
            c += 1

    if c == 1:
        return {}
    elif c >= 2:
        return None

    for i in range(n - 6):
        sub = feasible(i)
        if sub:
            return sub
    return None


assert proc(44, 'hfppoyeteeqfabac??ahjkrjdwa?a??bapnghixkweft') is not None

for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = proc(n, s)

    if ans is None:
        print('No')
        continue

    s = list(s)
    res = []
    for i in range(n):
        if s[i] != '?':
            res.append(s[i])
        elif i in ans:
            res.append(ans[i])
        else:
            res.append('z')

    print('Yes')
    print(''.join(res))
