for t in xrange(int(raw_input())):
    a, b, n = map(int, raw_input().split())
    c = a
    for i in xrange(n):
        c += pow(2, i) * b
        print c,
    print ''