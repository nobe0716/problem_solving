def solve(n, m, a):
    if m < n:
        return 0
    r = 1
    for i in range(n - 1):
        for j in range(i + 1, n):
            r = r * abs(a[i] - a[j]) % m
    return r


n, m = map(int, input().split())
a = list(map(int, input().split()))

r = solve(n, m, a)
print(r)
