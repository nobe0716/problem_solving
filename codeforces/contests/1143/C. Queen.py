# -*- coding:utf-8 -*-
"""
## Name of Prob
C. Queen

## Link
https://codeforces.com/contest/1143/problem/C

## Note
tree, 1...n

## Input
n; num of vertex
following n-line of p_i, c_i
p_i, c_i
- p_i; parent of v_i
- c_i; whether v_i respect its parent (0: respect, 1: does not respect

## Output
order of deletion to make graph full of respect

## Strategy
for all vertices, exclude who got any respect
filter who give no respect
then get intersection and sort
"""
from collections import defaultdict

n = int(input())
v = [0]
g = defaultdict(set)
root = None
is_candidates = [True] * (n + 1)
for i in range(1, n + 1):
    parent, respect = map(int, input().split())
    v.append([parent, respect])
    if respect == 0:
        is_candidates[parent] = False
    # g[parent].add(i)
    # if parent == -1:
    #     root = i

bad_sons = []

for i in range(1, n + 1):
    if is_candidates[i] and v[i][1] == 1:
        bad_sons.append(i)
if len(bad_sons) == 0:
    print(-1)
else:
    print(' '.join(map(str, sorted(bad_sons))))
