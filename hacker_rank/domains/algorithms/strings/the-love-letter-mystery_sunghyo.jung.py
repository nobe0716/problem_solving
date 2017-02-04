__author__ = 'sunghyo.jung'
for t in xrange(int(raw_input())):
    s = raw_input()
    print sum(map(lambda x: abs(ord(s[x]) - ord(s[len(s) - x - 1])), range(len(s)/2)))

