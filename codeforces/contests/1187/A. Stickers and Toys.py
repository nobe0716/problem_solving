"""
## Name of Prob
A. Stickers and Toys

## Link
https://codeforces.com/contest/1187/problem/0

## Note
n Kinder chocolate eggs
s stickers, t toys

for each kinder
- single sticker, no toy
- no sticker single toy
- both sticker and toy

## Input

## Output

minimum number of kinder surprise eggs
to sure that at leat one sticker and one toy

## Strategy

there exist (n - s) kinder which does not contains sticker
(n - t) kinder which does not contains toy

so if we buy max(n - s, n - t) + 1, then we have at least one sticker and toy
"""

n = int(input())
for _ in range(n):
    n, s, t = map(int, input().split())
    print(max(n - s, n - t) + 1)
