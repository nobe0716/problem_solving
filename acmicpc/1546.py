n = int(input())
a = [int(x) for x in input().split()]
m = max(a)
b = []
for e in a:
    b.append(e / m * 100)
print(sum(b) / n)
