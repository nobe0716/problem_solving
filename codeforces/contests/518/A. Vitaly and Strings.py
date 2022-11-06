# 2022-11-06 21:16:49.927793
# https://codeforces.com/problemset/problem/518/A
import sys

_DEBUG = False
_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(s, t):
    n = len(s)
    res = ''
    for i in range(n):
        if ord(t[i]) - ord(s[i]) > 1:
            res += chr(ord(s[i]) + 1) + 'a' * (n - i - 1)
            break
        elif ord(t[i]) == ord(s[i]) + 1:
            if not all(e == 'z' for e in s[i + 1:]):
                res = res + s[i] + 'z' * (n - i - 1)
                break
            elif not all(e == 'a' for e in t[i + 1:]):
                res = res + t[i] + 'a' * (n - i - 1)
                break
            else:
                return None
        else:
            res += s[i]
    if res < t:
        return res
    return None


assert proc('aba', 'aca') is not None

s = input()
t = input()

ans = proc(s, t)
if ans:
    print(ans)
else:
    print('No such string')
