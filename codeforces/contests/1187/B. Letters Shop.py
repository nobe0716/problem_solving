"""
## Name of Prob
B. Letters Shop

## Link
https://codeforces.com/contest/1187/problem/B

## Note
letters shop
n lowercase Latin letters
sold one by one from leftmost to rightmost
prefix of letters

m friends

## Input
n; 1 <= n <= 2 * 10^5
s; n-length str
m; 1 <= m <= 5 * 10^4
t_i ; 1 <= |t_i| <= 2 * 10^5 but sum(t_i) <= 2 * 10^5

## Output

m line of prefix should be bought

## Strategy
Store index of i-th letter position


"""
from collections import Counter, defaultdict

index_dict = defaultdict(list)

n = int(input())
s = input()
m = int(input())

for i, e in enumerate(s):
    index_dict[e].append(i)

for _ in range(m):
    t = input()
    c = Counter(t)
    print(max(index_dict[k][v - 1] for k, v in c.items()) + 1)
