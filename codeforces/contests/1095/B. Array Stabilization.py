n = int(input())
a = list(map(int, input().split()))
a = list(sorted(a))
if a[1] - a[0] > a[-1] - a[-2]:
    a = a[1:]
else:
    a = a[:-1]
print(a[-1] - a[0])
