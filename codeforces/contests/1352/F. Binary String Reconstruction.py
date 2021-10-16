# https://codeforces.com/problemset/problem/1352/F
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n0: int, n1: int, n2: int) -> str:
    prefix = (n0 + 1) * '0' if n0 > 0 else ''
    postfix = (n2 + 1) * '1' if n2 > 0 else ''

    ans = prefix + postfix
    if n0 > 0 and n2 > 0:  # 0011
        n1 -= 1
        if n1 > 0:
            ans += ('01' * (n1 // 2))
            if n1 % 2 == 1:
                ans += '0'
    elif n0 > 0:  # only 0000
        ans += ('10' * (n1 // 2))
        if n1 % 2 == 1:
            ans += '1'
    elif n2 > 0:  # only 1111
        ans += ('01' * (n1 // 2))
        if n1 % 2 == 1:
            ans += '0'
    else:  # empty
        ans = '01' * ((n1 + 1) // 2)
        if n1 % 2 == 0:
            ans += '0'
    return ans


def verify(ans, n0_expected, n1_expected, n2_expected):
    n0_actual = n1_actual = n2_actual = 0
    for i in range(1, len(ans)):
        if ans[i - 1:i + 1] == '00':
            n0_actual += 1
        elif ans[i - 1:i + 1] == '11':
            n2_actual += 1
        else:
            n1_actual += 1

    assert n0_expected == n0_actual
    assert n1_expected == n1_actual
    assert n2_expected == n2_actual


for _ in range(int(input())):
    n0, n1, n2 = [int(x) for x in input().strip().split()]
    ans = solve(n0, n1, n2)
    print(ans)

    # verify(ans, n0, n1, n2)
