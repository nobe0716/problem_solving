l = int(input())
n = input()
r = float('inf')

half = l // 2
if n[half] != '0':
    a, b = n[:half], n[half:]
    r = min(r, int(a) + int(b))

for i in range(half + 1, l):
    if n[i] != '0':
        a, b = n[:i], n[i:]
        r = min(r, int(a) + int(b))
        break
for i in range(half - 1, 0, -1):
    if n[i] != '0':
        a, b = n[:i], n[i:]
        r = min(r, int(a) + int(b))
        break
print(r)
