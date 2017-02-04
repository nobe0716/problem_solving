__author__ = 'sunghyo.jung'

def is_a_smaller(a, b):
    n = len(a)
    m = len(b)
    if n == m:
        return a < b
    elif n < m:
        return a < b[:n]
    else:
        return a[:m] <= b

for t in xrange(int(raw_input())):
    a, b = raw_input(), raw_input()
    c = ''

    while len(a) > 0 and len(b) > 0:
        if is_a_smaller(a, b):
            c += a[0]
            a = a[1:]
        else:
            c += b[0]
            b = b[1:]
    if len(a) == 0:
        c += b
    elif len(b) == 0:
        c += a
    print c