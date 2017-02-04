__author__ = 'sunghyo.jung'
from collections import Counter

n = int(input())
c = Counter([int(x) for x in input().split()])
for i in range(100):
    if i in c:
        print(c[i], end=' ')
    else:
        print('0', end=' ')
print('')

