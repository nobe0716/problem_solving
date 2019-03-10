from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)
for i in range(n - 1):
    for j in range(i + 1, n):
        d[a[i] + a[j]] += 1
print(max(d.values()))
