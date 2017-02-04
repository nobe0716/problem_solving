__author__ = 'sunghyo.jung'
t = int(raw_input().strip())
for a0 in xrange(t):
    n, c, m = map(int, raw_input().strip().split(' '))
    v = 0
    cnt = 0
    while n >= c:
        n -= c
        v += 1
        cnt += 1
        if cnt == m:
            cnt = 1
            v += 1
    print v

