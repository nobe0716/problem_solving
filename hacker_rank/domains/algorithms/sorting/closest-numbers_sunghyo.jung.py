__author__ = 'sunghyo.jung'

n = int(input())
ar = sorted([int(x) for x in input().split()])
idx = [0]
for i in range(n - 1):
    if ar[i + 1] - ar[i] < ar[idx[0] + 1] - ar[idx[0]]:
        idx = [i]
    elif ar[i + 1] - ar[i] == ar[idx[0] + 1] - ar[idx[0]]:
        idx.append(i)
for i in idx:
    print('%d %d' % (ar[i], ar[i + 1]), end=' ')