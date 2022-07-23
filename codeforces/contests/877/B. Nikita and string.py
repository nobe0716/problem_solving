# 2022-07-17T15:10:54Z
def proc(s):
    n = len(s)
    ac = [0] * (n + 1)
    bc = [0] * (n + 1)

    for i, e in enumerate(s):
        ac[i + 1] = ac[i]
        bc[i + 1] = bc[i]
        if e == 'a':
            ac[i + 1] += 1
        else:
            bc[i + 1] += 1

    res = max(ac[-1], bc[-1])

    for i in range(1, n + 1):
        res = max(res, bc[i] + ac[-1] - ac[i])

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            res = max(res, ac[i] + bc[j] - bc[i] + ac[-1] - ac[j])
    return res


s = input()
print(proc(s))
