n = int(input())
ar = map(int, raw_input().split())
d = []
for i in range(1, n):
    if ar[i] < ar[i - 1]:
        d.append(i)

if len(d) == 1:
    a, b = d[0] - 1, d[0]
    ar[a], ar[b] = ar[b], ar[a]
    if ar == sorted(ar):
        print("yes")
        print("swap %d %d" % (a + 1, b + 1))
    else:
        print("no")
elif len(d) == 2:
    a, b = d[0] - 1, d[1]
    ar[a], ar[b] = ar[b], ar[a]
    if ar == sorted(ar):
        print("yes")
        print("swap %d %d" % (a + 1, b + 1))
    else:
        print("no")
else:
    a = d[0] - 1
    b = d[len(d) - 1]
    if b - a != len(d):
        print("no")
    else:
        print("yes")
        print("reverse %d %d" % (a + 1, b + 1))

