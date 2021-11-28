a = int(input())
b = int(input())
c = int(input())
v = a * b * c
d = {x: 0 for x in range(10)}
while v > 0:
    d[v % 10] += 1
    v //= 10
for i in range(10):
    print(d[i])
