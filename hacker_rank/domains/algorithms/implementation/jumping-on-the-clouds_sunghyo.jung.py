def solve(n, clouds):
    p = 0
    c = 0
    while p < n - 1:
        if clouds[p + 2] == 1:
            p += 1
        else:
            p += 2
        c += 1
    return c

n = int(input())
clouds = list(map(int, input().split())) + [0]
print(solve(n, clouds))