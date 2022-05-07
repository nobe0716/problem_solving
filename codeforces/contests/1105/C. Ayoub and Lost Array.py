_MOD = 10 ** 9 + 7


def proc(n, l, r):
    t = [[0, 0, 0] for _ in range(n + 1)]
    m3 = (r // 3) - ((l - 1) // 3)
    m1 = (r + 2) // 3 - (l + 1) // 3
    m2 = (r + 1) // 3 - l // 3
    # t[1] = m3
    # t[2] = m3
    # for i in range(2, n + 1):
    t[1][0] = m3
    t[1][1] = m1
    t[1][2] = m2

    for i in range(2, n + 1):
        t[i][0] = (t[i - 1][1] * m2 + t[i - 1][2] * m1 + t[i - 1][0] * m3) % _MOD
        t[i][1] = (t[i - 1][1] * m3 + t[i - 1][2] * m2 + t[i - 1][0] * m1) % _MOD
        t[i][2] = (t[i - 1][1] * m1 + t[i - 1][2] * m3 + t[i - 1][0] * m2) % _MOD

    return t[n][0]


n, l, r = map(int, input().split())
ans = proc(n, l, r)
print(ans)
