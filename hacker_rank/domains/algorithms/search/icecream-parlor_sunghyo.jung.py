__author__ = 'sunghyo.jung'

for t in range(int(input())):
    m, n = int(input()), int(input())
    c = [int(x) for x in input().split()]
    di = {}
    for i in range(len(c)):
        if c[i] not in di:
            di[c[i]] = []
        di[c[i]].append(i + 1)

    for v in sorted(di.keys()):
        if m == v * 2 and len(di[v]) >= 2:
            print('%d %d' % (di[v][0], di[v][1]))
            break
        elif (m - v) in di:
            r = sorted([di[v][0], di[m - v][0]])
            print('%d %d' % (r[0], r[1]))
            break
