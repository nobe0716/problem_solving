# https://codeforces.com/problemset/problem/1249/C2
"""
good numbers; it can be represented as a sum of distinct powers of 3

means that it is represented with 1 or 0 on 3 (3)

3 ** i <= n < 3 ** (i + 1)

create three base representation, regard this as binary and add one
"""
import sys

_DEBUG = False
# _DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n):
    def num_to_str(n):
        nums = []
        while n > 0:
            n, r = divmod(n, 3)
            nums.append(r)
        return ''.join(str(i) for i in reversed(nums))

    def str_to_num(s):
        num = 0
        for e in s:
            num = num * 3 + int(e)
        return num

    s = num_to_str(n)
    if '2' not in s:
        return n
    s = list(s)
    index_of_two = s.index('2')
    s[index_of_two + 1:] = ['0'] * (len(s) - index_of_two - 1)
    while index_of_two > 0:
        if s[index_of_two] == '0':
            s[index_of_two] = '1'
            break
        s[index_of_two] = '0'
        index_of_two -= 1
    if index_of_two == 0:
        s[0] = '0'
        s = ['1'] + s

    res = str_to_num(''.join(s))
    # print(res)
    return res


if _DEBUG:
    assert solve(3620) == 6561
    assert solve(14) == 27
    assert solve(2) == 3
    assert solve(2944) == 2944
    assert solve(13) == 13
    assert solve(1) == 1
    assert solve(6) == 9
    assert solve(10000) == 19683
    assert solve(1000000000000000000) == 1350851717672992089

for _ in range(int(input())):
    n = int(input())
    ans = solve(n)
    print(ans)
