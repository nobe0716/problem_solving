from collections import Counter
for t in range(int(input())):
    n = int(input())
    a = map(int, raw_input().split())
    c = Counter(a)
    r = 0
    for k in c.keys():
        v = c[k]
        r += v * (v - 1)
    print(r)