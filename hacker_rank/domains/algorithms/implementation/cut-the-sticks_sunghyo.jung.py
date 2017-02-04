__author__ = 'sunghyo.jung'
n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
while len([x for x in arr if x > 0]):
    print len([x for x in arr if x > 0])
    v = min([x for x in arr if x > 0])
    arr = [x - v]) for x in arr]