from collections import Counter


def solve(n, k, a):
    c = Counter(a)
    r = 0
    rests = 0
    for k, v in c.items():
        r += (v // 2 * 2)
        rests += (v % 2)
    return r + (rests + 1) // 2


n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
r = solve(n, k, a)
print(r)
