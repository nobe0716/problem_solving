# 2022-06-12T07:58:56.404Z


def proc(n, k, a, b):
    h = []
    v = []
    for i in range(n):
        r, m = divmod(b[i], a[i])
        v.append([r, a[i] - m, a[i]])

    v = sorted(v, reverse=True)

    while len(v) > 1:
        r2, m2, c2 = v.pop()
        r1, m1, c1 = v.pop()

        diff = r1 - r2
        cost = m2 + (diff - 1) * c2

        if k >= cost:
            k -= cost

            v.append((r1, m1 + c2, c1 + c2))
        else:
            if k > m2:
                k -= m2
                r2 += 1
            return r2 + k // c2

    r2, m2, c2 = v.pop()
    if k > m2:
        k -= m2
        r2 += 1
    return r2 + k // c2


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = proc(n, k, a, b)
print(ans)
