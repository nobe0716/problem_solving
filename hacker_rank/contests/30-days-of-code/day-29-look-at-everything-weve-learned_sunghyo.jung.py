__author__ = 'sunghyo.jung'

def is_funny(s):
    r = s[::-1]
    #print [abs(ord(s[i]) - ord(s[i - 1])) == abs(ord(r[i]) - ord(r[i - 1])) for i in range(1, len(s))]
    return all([abs(ord(s[i]) - ord(s[i - 1])) == abs(ord(r[i]) - ord(r[i - 1])) for i in range(1, len(s))])

for t in xrange(int(raw_input())):
    print "Funny" if is_funny(raw_input()) else "Not Funny"
