__author__ = 'sunghyo.jung'
for t in xrange(int(raw_input())):
    s = raw_input()

    r = s[::-1]
    for i in xrange(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            print 'Not',
            break
    print 'Funny'
