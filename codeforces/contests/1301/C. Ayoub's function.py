# 2022-09-04 15:27:04.802963
# https://codeforces.com/problemset/problem/1301/C
import sys

_DEBUG = False
_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


"""
6 2

7 // 3 == 2


001001 3 + 3

001010 3 + 1 + 1 

"""
def proc(n, m):
    f = lambda x: x * (x + 1) // 2
    if n == m:
        return n * (n + 1) // 2
    elif m == 0:
        return 0

    total = n * (n + 1) // 2
    if m == 1:
        left_zero = n // 2
        right_zero = (n + 1) // 2 - 1
        return total - f(left_zero) - f(right_zero)
    elif m <= n // 2:
        """
        single set
        
        x zeroes 1 ones
        
        n >= (x + 1) * m
        (x + 1) <= n / m
        
        
        0 0
        
        
        x == n // m - 1
        num of sets = n // (x + 1)
        remain zeroes = n % (x + 1)
        """

        x = max(1, (n + 1) // (m + 1) - 1)
        num_of_set = n // (x + 1)
        remain_zeroes = n % (x + 1)

        res = total - num_of_set * f(x) - f(remain_zeroes)
        return res
    else:
        """
        n - m 0's remain
        """
        return total - (n - m)


if _DEBUG:
    assert proc(3, 1) == 4
    assert proc(2, 1) == 2
    assert proc(5, 1) == 9
    assert proc(3, 3) == 6
    assert proc(4, 0) == 0
    assert proc(5, 2) == 12

    fin = open('input.txt')
    fou = open('output.txt')

    fin.readline()
    for line in fin.readlines():
        n, m = map(int, line.split())

        expected = int(fou.readline())

        if proc(n, m) != expected:
            print('proc({}, {}) != {} !!'.format(n, m, expected))


for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = proc(n, m)
    if not _DEBUG:
        print(str(ans) + '\n')
    else:
        print(ans)
