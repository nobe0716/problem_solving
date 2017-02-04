__author__ = 'sunghyo.jung'
p, q = int(raw_input()), int(raw_input())

def is_kaprekar(n):
    if n == 1:
        return True
    d = len(str(n))
    s = str(n * n)
    d = len(s) - d
    a = int(s[:d] if len(s[:d]) > 0 else '0')
    b = int(s[d:] if len(s[d:]) > 0 else '0')
    return n == a + b and b > 0

flag = False
for i in range(p, q + 1):
    if is_kaprekar(i):
        flag = True
        print i,
if flag:
    print ''
else:
    print 'INVALID RANGE'