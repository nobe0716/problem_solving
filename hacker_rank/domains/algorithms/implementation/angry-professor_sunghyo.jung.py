__author__ = 'sunghyo.jung'

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    for time in a:
        if time <= 0: # attend!
            k -= 1
    if k > 0: # need more attend to start class
        print "YES"
    else:
        print "NO"