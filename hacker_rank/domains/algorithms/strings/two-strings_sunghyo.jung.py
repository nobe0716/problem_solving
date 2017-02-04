__author__ = 'sunghyo.jung'
for t in xrange(int(raw_input())):
    a = set(raw_input())
    b = set(raw_input())
    print 'YES' if len(filter(lambda x:x in b, a)) > 0 else 'NO'