def solve(n, m, k, h):
    for i in range(n - 1):
        cost = h[i + 1] - k - h[i]
        if cost < 0:
            m += min(h[i], -cost)
        elif cost > m:
            return False
        else:
            m -= cost
    return True


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    h = list(map(int, input().split()))
    r = solve(n, m, k, h)
    print('YES' if r else 'NO')
