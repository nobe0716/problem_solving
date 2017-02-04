__author__ = 'sunghyo.jung'

n, t = map(int, raw_input().split())
l = map(int, raw_input().split())
for test in xrange(t):
    a, b = map(int, raw_input().split())
    v = min(l[a:b+1])
    print v
