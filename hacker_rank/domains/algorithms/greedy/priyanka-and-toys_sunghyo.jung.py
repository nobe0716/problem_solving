__author__ = 'sunghyo.jung'
n = input()
a = sorted([int(x) for x in input().split()])
c = 1
w0 = a[0]
for w in a:
    if w > w0 + 4:
        c += 1
        w0 = w
print(c)

