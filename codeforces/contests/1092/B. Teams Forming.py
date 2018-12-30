n = int(input())
a = list(sorted(list(map(int, input().split()))))
c = 0
for i in range(0, n, 2):
    c += (a[i + 1] - a[i])
print(c)
