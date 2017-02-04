__author__ = 'sunghyo.jung'
n, k = [int(x) for x in input().split()]
c = sorted([int(x) for x in input().split()], reverse=True)
buckets = [[] for x in range(k)]
for i in range(len(c)):
    buckets[i % k].append(c[i])
price = 0
for bucket in buckets:
    for j in range(len(bucket)):
        price += (j + 1) * bucket[j]
print(price)