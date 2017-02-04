__author__ = 'sunghyo.jung'
import itertools
from collections import Counter

for i in xrange(int(raw_input())):
    s = raw_input()
    r = 0
    d = dict()

    for c in [Counter(sorted(s[a:b])) for [a, b] in itertools.combinations(range(len(s) + 1), 2)]:
        if d.has_key(str(c)):
            d[str(c)] += 1
        else:
            d[str(c)] = 1
    for v in d.values():
        if v >= 2:
            r += (v * (v - 1)) / 2
    print r