# https://codeforces.com/contest/276/problem/C
import sys
from collections import defaultdict

input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
d = defaultdict(int)
count_per_stack = defaultdict(int)
for _ in range(q):
    li, ri = map(int, input().split())
    d[li] += 1
    d[ri + 1] -= 1

    # if d[li] == 0:
    #     del d[li]
    # if d[ri] == 0:
    #     del d[ri]

for k in set(d.keys()):
    if d[k] == 0:
        del d[k]

current_stack = 0
last_key = None
for k in sorted(d.keys()):
    next_stack = current_stack + d[k]

    if current_stack > 0:
        count_per_stack[current_stack] += (k - last_key)

    last_key = k
    current_stack = next_stack

a.sort(reverse=True)
idx = 0
res = 0
for k in sorted(count_per_stack.keys(), reverse=True):
    res = res + sum(a[idx:idx + count_per_stack[k]]) * k
    idx += count_per_stack[k]

# print(d)
# print(count_per_stack)
print(res)
