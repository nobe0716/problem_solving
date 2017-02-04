__author__ = 'sunghyo.jung'
n = int(input())

table = {}
for i in range(1, n + 1):
    t, d = [int(x) for x in input().split()]
    k = t + d
    if k not in table:
        table[k] = []
    table[k].append(i)
for k in sorted(table.keys()):
    for i in table[k]:
        print(i, end=' ')

