# https://codeforces.com/problemset/problem/1296/D
import math
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline

n, a, b, k = map(int, input().strip().split())
h = [int(x) for x in input().strip().split()]

initial_points = 0
required_k = []
for e in h:
    mod_val = e % (a + b)
    if 0 < mod_val <= a:
        initial_points += 1
    else:
        mod_val = (a + b) if mod_val == 0 else mod_val
        required_k.append(int(math.ceil(mod_val / a)) - 1)

additional_points = 0
for e in sorted(required_k):
    if k < e:
        break
    k -= e
    additional_points += 1

print(initial_points + additional_points)
