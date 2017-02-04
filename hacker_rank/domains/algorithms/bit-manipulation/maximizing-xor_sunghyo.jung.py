__author__ = 'sunghyo.jung'
l, r = int(input()), int(input())
v = -1

for a in range(l, r + 1):
    for b in range(a, r + 1):
        v = max([v, a ^ b])
print (v)
