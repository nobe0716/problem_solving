__author__ = 'sunghyo.jung'
t = int(raw_input())

def back(n, a, b, v):
    if n == 1:
        return [v]
    return back(n - 1, a, b, v + a) + back(n - 1, a, b, v + b)
for test in xrange(t):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    s = set()

    for i in range(n):
        s.add(a * i + b * (n - i - 1))
    for v in sorted(s):
        print v,
    print ''
