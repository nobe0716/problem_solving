__author__ = 'sunghyo.jung'
n = int(raw_input())
a = sorted(map(int, raw_input().split()))

min_idx = [0]
min_val = a[1] - a[0]

for i in xrange(n - 1):
    if min_val > abs(a[i + 1] - a[i]):
        min_val = abs(a[i + 1] - a[i])
        min_idx = [i]
    elif min_val == abs(a[i + 1] - a[i]):
        min_idx.append(i)
for i in min_idx:
    print a[i], a[i + 1],
print ''
