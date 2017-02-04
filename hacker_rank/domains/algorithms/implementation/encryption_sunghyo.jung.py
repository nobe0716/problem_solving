__author__ = 'sunghyo.jung'

import math
import sys

def get_rc(s):
    l = len(s)
    minimum = int(math.floor(math.sqrt(l)))
    maximum = int(math.ceil(math.sqrt(l)))
    possible_rc = []
    for r in range(minimum, maximum + 1):
        for c in range(r, maximum + 1):
            if r * c >= l:
                possible_rc.append([r,c])
    ret = possible_rc.pop()
    for r, c in possible_rc:
        if ret[0] * ret[1] > r * c:
            ret = [r, c]
    return ret

s = raw_input()
s = s.replace(' ', '')
r, c = get_rc(s)
e = []

for i in xrange(r):
    e.append(s[:c])
    s = s[c:]

for j in xrange(c):
    for i in xrange(r):
        if len(e[i]) > j and len(e[i][j]) > 0:
            sys.stdout.write(e[i][j])
    print ' ',
print ''