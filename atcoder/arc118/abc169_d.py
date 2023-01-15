from collections import Counter

op = 0
n = int(input())
s = set()

c = Counter()
i = 2
while i ** 2 < n:
    while n % i == 0:
        c[i] += 1
        n //= i
    i += 1
if n > 1:
    c[n] += 1

res = 0
for k, v in c.items():
    i = 1
    while v >= i:
        v -= i
        i += 1
        res += 1

print(res)
