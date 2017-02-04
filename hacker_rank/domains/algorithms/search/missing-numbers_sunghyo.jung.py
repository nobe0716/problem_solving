from collections import Counter

n = int(input())
a = [int(x) for x in raw_input().split()]
m = int(input())
b = [int(x) for x in raw_input().split()]
a = Counter(a)
b = Counter(b)

for elem in b.keys():
    if elem not in a or a[elem] < b[elem]:
        print elem,
print ''