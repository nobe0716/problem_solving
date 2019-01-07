from collections import Counter

n, k = list(map(int, input().split()))
s = bin(n)[2:]
c = Counter(s)
if k > n or c['1'] > k:
    print('NO')
else:
    print('YES')
    c = Counter()
    i = 1
    t = 0
    for e in reversed(s):
        if e == '1':
            c[i] += 1
            t += 1
        i *= 2
    max_i = i
    while t < k:
        if c[i] == 0:
            i //= 2
            continue
        if c[i] + t <= k:
            c[i // 2] += c[i] * 2
            t += c[i]
            c[i] = 0
            i //= 2
        else:
            c[i // 2] += (k - t) * 2
            c[i] -= (k - t)
            break
    i = 1
    r = []
    while i <= max_i:
        if c[i] > 0:
            r += [i] * c[i]
        i *= 2
    print(' '.join(map(str, r)))
