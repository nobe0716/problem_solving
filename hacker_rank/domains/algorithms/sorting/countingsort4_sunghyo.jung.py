__author__ = 'sunghyo.jung'
n = int(input())

d = {}
for i in range(n):
    num, name = input().split()
    num = int(num)
    if num not in d:
        d[num] = []

    if i < n / 2:
        d[num].append('-')
    else:
        d[num].append(name)

for k in sorted(d.keys()):
    for elem in d[k]:
        print(elem, end=' ')
print()


