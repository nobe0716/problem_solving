d = {}
n = int(raw_input())
for t in xrange(n):
    k = raw_input()
    d[k] = raw_input()
for t in xrange(n):
    k = raw_input()
    if k not in d:
        print 'Not found'
    else:
        print k + '=' + d[k]
