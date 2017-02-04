__author__ = 'sunghyo.jung'
for t in xrange(int(raw_input())):
    s = raw_input()

    a = 0
    c = 'A'
    for ch in s:
        if ch != c:
            a += 1
        else:
            c = 'B' if c == 'A' else 'A'

    b = 0
    c = 'B'
    for ch in s:
        if ch != c:
            b += 1
        else:
            c = 'B' if c == 'A' else 'A'
    print min([a, b])