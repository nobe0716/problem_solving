# 2022-11-06 21:34:05.207933
# https://codeforces.com/problemset/problem/246/D
import sys
from collections import defaultdict

_DEBUG = True
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write

g = defaultdict(set)
n, m = map(int, input().split())
c = [0] + list(map(int, input().split()))
colors = set(c[1:])
diversity = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())

    color_a = c[a]
    color_b = c[b]

    if color_a != color_b:
        diversity[color_a].add(color_b)
        diversity[color_b].add(color_a)

max_color = min(colors)
for color in colors:
    if len(diversity[color]) > len(diversity[max_color]):
        max_color = color
    elif len(diversity[color]) == len(diversity[max_color]):
        max_color = min(max_color, color)
print(max_color)
