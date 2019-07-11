from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    mods = map(lambda x: x % 3, a)
    c = Counter(mods)

    while c[1] > 0 and c[2] > 0:
        c[0] += 1
        c[1] -= 1
        c[2] -= 1
    while c[1] >= 3:
        c[0] += 1
        c[1] -= 3
    while c[2] >= 3:
        c[0] += 1
        c[2] -= 3
    print(c[0])
