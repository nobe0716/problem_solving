def solve(n, a):
    b = [None] * n
    u = set(a)
    for i in range(1, n):
        if a[i] > a[i - 1]:
            b[i] = a[i - 1]
        if a[i] > i + 1:
            return -1

    j = 0
    for i in range(n):
        if b[i] is not None:
            continue
        while j in u:
            j += 1
        b[i] = j
        u.add(j)

    return ' '.join(map(str, b))


n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
