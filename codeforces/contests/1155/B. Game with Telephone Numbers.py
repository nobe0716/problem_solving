"""
## Name of Prob
B. Game with Telephone Numbers

## Link
https://codeforces.com/contest/1155/problem/B

## Note
A telephone number is a sequence of exactly 11 digits such that its first digit is 8.

## Input

## Output

## Strategy
there is (n - 12) turns to determine
after (n - 12) turns, if there must be 88[0-9]{12} then Vasya win

Petya will move to remove every 8

count[8] < (n - 12) // 2 => NO because he will remove all 8's

Petya will remove leading 8's
Vasya remove not 8 letter from first

count number of 8's until found (turn + 1) // 2 not '8' s
"""
from collections import Counter

_DEBUG = True


def solve(n, s):
    c = Counter(s)
    turn_count = n - 12
    if c['8'] < turn_count // 2:
        return 'NO'

    v_count = 0
    eight_count = 0
    for i in range(n):
        if s[i] != '8':
            v_count += 1
            if v_count >= (turn_count + 1) // 2:
                j = i + 1
                while j < n and s[j] == '8':
                    eight_count += 1
                    j += 1
                break
        else:
            eight_count += 1
    # print(eight_count, turn_count)
    if eight_count >= turn_count // 2 + 2:
        return 'YES'
    return 'NO'


assert solve(13, '8380011223344') == 'YES'
assert solve(15, '807345619350641') == 'NO'
assert solve(29, '88811188118181818118111111111') == 'NO'
assert solve(19, '8181818181111111111') == 'YES'
assert solve(13, '9999999998888') == 'NO'
assert solve(13, '0000008888888') == 'NO'
assert solve(13, '2480011223348') == 'NO'
assert solve(17, '87879887989788999') == 'YES'

n = int(input())
s = input()
solution = solve(n, s)
print(solution)
