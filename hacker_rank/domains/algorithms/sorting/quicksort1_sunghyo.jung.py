__author__ = 'sunghyo.jung'
n = int(input())
ar = [int(x) for x in input().split()]

pivot = ar[0]
left = []
right = []
for a in ar:
    if a >= pivot:
        right.append(a)
    else:
        left.append(a)
print(" ".join(map(str, left + right)))