"""
WIP
"""
from collections import Counter

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
c = Counter(a)

optimal_count = n // k
top_ks = c.most_common(k)

r = []
for top_k in top_ks:
    r += [top_k[0]] * max(top_k[1] // optimal_count, 1)
r = r[:k]
print(' '.join(map(str, r)))
