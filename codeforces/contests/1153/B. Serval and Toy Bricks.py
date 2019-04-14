"""
## Name of Prob
B. Serval and Toy Bricks

## Link
https://codeforces.com/contest/1153/problem/B

## Note
restore original 3-D by front left top view

## Input
n, m, h

## Output

## Strategy
easy, set Grid[i][j] should be min(a[j], b[i])
"""

_DEBUG = True
# length, width, height
n, m, h = map(int, input().split())
#  left to right of the front view (0≤ai≤h).
a = list(map(int, input().split()))
# height in the j-th column from left to right of the left view.
b = list(map(int, input().split()))

top_view = [list(map(int, input().split())) for _ in range(n)]
top_confirmed = [[True] * m for _ in range(n)]

block_count = 0
for i in range(n):
    for j in range(m):
        if top_view[i][j] == 1:
            top_view[i][j] = min(a[j], b[i])

for i in range(n):
    print(' '.join(map(str, top_view[i])))
