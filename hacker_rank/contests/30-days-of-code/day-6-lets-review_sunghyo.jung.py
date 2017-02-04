import sys

n = int(raw_input().strip())
for i in xrange(n):
    for j in xrange(n - i):
        print '',
    for j in xrange(i + 1):
        sys.stdout.write('#')
    print ''
