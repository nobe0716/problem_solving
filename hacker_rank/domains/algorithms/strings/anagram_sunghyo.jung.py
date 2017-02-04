__author__ = 'sunghyo.jung'
from collections import Counter

for t in xrange(int(raw_input())):
    s = raw_input()
    if len(s) % 2 == 1:
        print -1
        continue
    a = Counter(s[len(s)/2:])
    b = Counter(s[:len(s)/2])
    c = sum((a - b).values())
    print c