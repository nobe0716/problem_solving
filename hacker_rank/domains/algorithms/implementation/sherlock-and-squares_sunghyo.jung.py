__author__ = 'sunghyo.jung'

import math

t = int(raw_input())
for test_case in xrange(t):
    a, b = map(int, raw_input().split())
    c = 0
    for i in range(int(math.floor(math.sqrt(a))), int(math.floor(math.sqrt(b)) + 1)):
        #print i
        if a <= i * i <= b:
            c += 1
    print c


