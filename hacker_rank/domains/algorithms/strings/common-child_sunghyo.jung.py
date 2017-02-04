__author__ = 'sunghyo.jung'

a, b = raw_input(), raw_input()

n = len(a)
m = len(b)
t = [[0 for i in xrange(m)] for j in xrange(n)]

for i in xrange(n):
    t[i][0] = 1 if a[i] == b[0] else 0
for i in xrange(m):
    t[0][i] = 1 if a[0] == b[i] else 0

for i in xrange(1, n):
    for j in xrange(1, m):
        if a[i] == b[j]:
            t[i][j] = t[i - 1][j - 1] + 1
        elif t[i - 1][j] > t[i][j - 1]:
            t[i][j] = t[i - 1][j]
        else:
            t[i][j] = t[i][j - 1]
print t[n - 1][m - 1]

