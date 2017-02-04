__author__ = 'sunghyo.jung'

# https://www.hackerrank.com/challenges/maxsubarray

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(t):
        n = int(raw_input())
        a = map(int,raw_input().strip().split(' '))

        s = [a[0]]
        z = max([a[0], 0])

        for j in xrange(1, n):
            s.append(max([s[j - 1] + a[j], a[j]]))
            if a[j] > 0:
                z += a[j]

        if z == 0:
            z = max(a)
        print str(max(s))+' '+str(z)