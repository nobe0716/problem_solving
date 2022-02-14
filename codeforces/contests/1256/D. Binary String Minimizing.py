# 2022-02-13 21:52:55.950959
# https://codeforces.com/problemset/problem/1256/D
import sys
from collections import deque

_DEBUG = True
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, k, s):
    q = deque()
    arr = list(s)
    for i in range(n):
        if arr[i] == '0':
            q.append(i)

    for i in range(n):
        if arr[i] == '0':
            continue
        while q and q[0] <= i:
            q.popleft()
        if k == 0 or len(q) == 0:
            break
        if q[0] - i > k:
            continue
        arr[i] = '0'
        arr[q[0]] = '1'
        k -= (q[0] - i)
        q.popleft()

    res = ''.join(arr)
    # if _DEBUG:
    #     print(res)
    return res


if _DEBUG:
    #                                  00110110
    assert solve(10, 2, '1001001000') == '0011001000'
    assert solve(8, 5, '11011010') == '01011110'
    assert solve(9, 1, '000010101') == '000001101'
    assert solve(7, 11, '1111100') == '0011111'
    assert solve(7, 9, '1111100') == '0101111'
    assert solve(3, 3, '111') == '111'

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    ans = solve(n, k, s)

    print(ans)
