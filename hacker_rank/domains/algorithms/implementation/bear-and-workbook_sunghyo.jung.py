__author__ = 'sunghyo.jung'
n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

r = 0
p = 1
for c in a:
    for i in range(1, c + 1):
        if p == i:
            r += 1
        if i % k == 0 and i != 0 and i != c:
            p += 1
    p += 1
print(r)


