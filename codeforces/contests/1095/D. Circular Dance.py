n = int(input())
a = [[0, 0]]

d = {}  # from -> to
for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(1, n + 1):
    first, second = a[i]
    if i in d:
        if d[i] == first:
            d[first] = second
        elif d[i] == second:
            d[second] = first
    elif second in a[first]:
        d[i] = first
        d[first] = second
    elif first in a[second]:
        d[i] = second
        d[second] = first

r = [1]
for _ in range(n - 1):
    r.append(d[r[-1]])
print(' '.join(map(str, r)))
