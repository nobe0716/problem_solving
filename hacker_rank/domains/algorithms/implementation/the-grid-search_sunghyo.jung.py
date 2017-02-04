__author__ = 'Naver'

import sys


'''
You may run this edge case when test#5 fails

1
4 6
123412
561212
123634
781288
2 2
12
34

'''

t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
        G_t = str(raw_input().strip())
        G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        P.append(P_t)

    exist = False

    for i in xrange(R - r + 1):
        for j in xrange(C - c + 1):
            match = True
            for k in xrange(r):
                if G[i + k][j:j+c] != P[k]:
                    match = False
                    break
            if match:
                exist = True
                break
        if exist:
            break

    if exist:
        print "YES"
    else:
        print "NO"