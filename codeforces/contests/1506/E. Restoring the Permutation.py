# 2022-02-20 15:49:52.339135
# https://codeforces.com/problemset/problem/1506/E
import bisect
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


def proc(n, a):
    min_array = [0] * n
    max_array = [0] * n

    num_set = set(range(1, n + 1))
    min_array[0] = max_array[0] = a[0]
    num_set.remove(a[0])

    pos_array = []

    for i in range(1, n):
        if a[i] != a[i - 1]:
            min_array[i] = max_array[i] = a[i]
            num_set.remove(a[i])
        else:
            pos_array.append(i)

    numbers = sorted(num_set)

    for i, v in zip(pos_array, numbers):
        min_array[i] = v

    j = 0
    max_val = 0
    for i in range(n):
        if max_array[i] != 0:
            if max_val + 1 < max_array[i]:
                j = bisect.bisect_left(numbers, max_array[i]) - 1
            max_val = max_array[i]
        else:
            while numbers[j] not in num_set:
                j -= 1
            max_array[i] = numbers[j]
            num_set.remove(numbers[j])
    return min_array, max_array


# print(proc(2 * 10 ** 5, list(range(1, 2 * 10 ** 5 + 1)))[0])
# print(proc(2 * 10 ** 5, list(range(1, 2 * 10 ** 5 + 1)))[1])

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = proc(n, a)

    if _DEBUG:
        print(' '.join(map(str, ans[0])))
        print(' '.join(map(str, ans[1])))
    else:
        print(' '.join(map(str, ans[0])) + '\n')
        print(' '.join(map(str, ans[1])) + '\n')
