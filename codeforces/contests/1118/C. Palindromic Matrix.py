from collections import Counter

n = int(input())
s = list(map(int, input().split()))
c = Counter(s)
m = {}

two_pos = []
four_pos = []
one_pos = []

if n % 2 == 1:
    one_pos.append((n // 2, n // 2))
    for i in range(n // 2):
        two_pos.append(((i, n // 2), (n - i - 1, n // 2)))
        two_pos.append(((n // 2, i), (n // 2, n - i - 1)))
for i in range(n // 2):
    for j in range(n // 2):
        four_pos.append(((i, j), (i, n - j - 1), (n - i - 1, j), (n - i - 1, n - j - 1)))

IS_POSSIBLE = True
for k, v in c.items():
    if v % 2 == 1:
        if len(one_pos) == 0:
            IS_POSSIBLE = False
            break
        pos = one_pos.pop()
        m[pos] = k
        v -= 1

    while v >= 4 and len(four_pos) > 0:
        for e in four_pos.pop():
            m[e] = k
        v -= 4
    while v >= 2 and len(two_pos) > 0:
        for e in two_pos.pop():
            m[e] = k
        v -= 2
    if v > 0:
        IS_POSSIBLE = False
        break

if not IS_POSSIBLE:
    print('NO')
else:
    print('YES')
    for i in range(n):
        for j in range(n):
            print(m[(i, j)], end=' ')
        print()
