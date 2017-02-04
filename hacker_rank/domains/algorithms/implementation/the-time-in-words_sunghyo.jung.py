__author__ = 'sunghyo.jung'
h = int(raw_input().strip())
m = int(raw_input().strip())

num = ['o\' clock', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
if m == 0:
    print '%s %s' % (num[h], num[m])
elif m == 1:
    print '%s minute past %s' % (num[m], num[h])
elif m < 15:
    print '%s minutes past %s' % (num[m], num[h])
elif m == 15:
    print '%s past %s' % (num[m], num[h])
elif m < 20:
    print '%s minutes past %s' % (num[m], num[h])
elif m < 30:
    print 'twenty %s minutes past %s' % (num[m - 20], num[h])
elif m == 30:
    print 'half past %s' % (num[h])
elif m < 40:
    print 'twenty %s minutes to %s' % (num[60 - m - 20], num[h + 1])
elif m < 45:
    print '%s minutes to %s' % (num[60 - m], num[h + 1])
elif m == 45:
    print '%s to %s' % (num[60 - m], num[h + 1])
elif m < 59:
    print '%s minutes to %s' % (num[60 - m], num[h + 1])
else:
    print '%s minute to %s' % (num[60 - m], num[h + 1])