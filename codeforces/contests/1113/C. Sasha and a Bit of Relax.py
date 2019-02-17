from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
t = [0] * n
t[0] = a[0]
for i in range(1, n):
    t[i] = t[i - 1] ^ a[i] # a_i ^...^ a_j = t[j] ^ t[i]
r = {0: defaultdict(int), 1: defaultdict(int)}
r[1][0] = 1
res = 0
for i in range(n):
    res += r[i % 2][t[i]]
    r[i % 2][t[i]] += 1
print(res)