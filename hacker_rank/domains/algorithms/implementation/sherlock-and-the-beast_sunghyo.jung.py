#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    found = False
    for b in xrange(0, n/5 + 1):
        #print "current b : %d" % b
        if (n - 5 * b) % 3 == 0:
            a = (n - 5 * b) / 3
            #print "found a:%d, b:%d" % (a, b)
            found = True;
            print '5' * (a* 3) + '3' * (b * 5)
            break
    if not found:
        print "-1"
