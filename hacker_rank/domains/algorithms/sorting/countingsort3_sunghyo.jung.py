__author__ = 'sunghyo.jung'
n = int(input())

d = {}
for i in range(n):
    num, name = input().split()
    num = int(num)
    if num not in d:
        d[num] = 0
    d[num] += 1

c = 0
for i in range(100):
    if i in d:
        c += d[i]
    print(c, end=' ')
print()

