# 2022-04-24 19:35:32.735924
# https://codeforces.com/problemset/problem/1511/D
import string
import sys
from collections import Counter

n, k = map(int, input().split())

c = Counter()

cur = 'a'
candidates = string.ascii_lowercase[:k]
for i in range(1, k):
    e = chr(ord('a') + i)
    new = ''
    for j in range(1, i + 1):
        new += e + chr(ord('a') + j)
    new += 'a'
    cur += new

ans = ''

if n > len(cur):
    ans = cur * (n // len(cur)) + cur[:n % len(cur)]
else:
    ans = cur[:n]

sys.stdout.write(ans + '\n')
