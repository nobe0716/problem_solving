# -*- coding:utf-8 -*-
"""
## Name of Prob
A. The Doors

## Link
https://codeforces.com/contest/1143/problem/A

## Note
may be it will be ok if all integer become 0 or 1

## Input
n; total len
n integers; 0 or 1

## Output
smallest k

## Strategy
just find first num which is different with last one.
"""

n = int(input())
a = list(map(int, input().split()))
k = n - 2
while k >= 0 and a[k] == a[-1]:
    k -= 1
print(k + 1)
