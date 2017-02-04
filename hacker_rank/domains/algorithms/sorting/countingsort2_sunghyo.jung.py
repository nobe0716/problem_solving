__author__ = 'sunghyo.jung'
from collections import Counter

n = int(input())
c = Counter([int(x) for x in input().split()])
for i in range(100):
    if i in c:
        print((str(i) + ' ') * c[i], end='')
print('')
'''
n = int(input())
ar = [int(x) for x in input().split()]
print(' '.join(map(str, sorted(ar))))
'''