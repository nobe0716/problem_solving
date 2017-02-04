__author__ = 'sunghyo.jung'
t = int(raw_input())
gems = raw_input()
for i in xrange(1, t):
    s = raw_input()
    gems = filter(lambda x: x in s, gems)
print len(set(gems))