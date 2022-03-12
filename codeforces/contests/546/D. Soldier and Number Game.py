# 2022-03-12 16:48:29.943087
# https://codeforces.com/problemset/problem/546/D
# Timeout but IO matters
import sys

maximum_value_a = 5000001
# maximum_value_a = 10

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write

LIMIT = 2238
primes = set(range(2, LIMIT))

for i in range(2, LIMIT):
    if i not in primes:
        continue
    for j in range(i * 2, LIMIT, i):
        primes.discard(j)
primes = sorted(primes)

t = [1] * maximum_value_a
t[0] = 0

for i in range(4, maximum_value_a):
    if i in primes:
        continue
    for p in primes:
        if i % p != 0:
            continue
        t[i] = t[i // p] + 1
        break
for i in range(2, maximum_value_a):
    t[i] = t[i - 1] + t[i]


# acc_sum = [0] * maximum_value_a
# for i in range(1, maximum_value_a):
#     acc_sum[i] = acc_sum[i - 1] + t[i]


def proc(a, b):
    return t[a] - t[b]


if _DEBUG:
    assert proc(3, 1) == 2
    assert proc(6, 3) == 5
    assert proc(1000003, 1000002) == 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    if _DEBUG:
        print(proc(a, b))
    else:
        print(str(proc(a, b)) + '\n')
