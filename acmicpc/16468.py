M = 100030001

t = {}


def s(n, l):
    if (n, l) in t:
        return t[(n, l)]
    elif n > 2 ** l - 1:
        return 0
    elif n == 0:
        return 1
    elif n <= 2:
        return n

    ans = sum(s(x, l - 1) * s(n - x - 1, l - 1) for x in range(n // 2)) * 2 % M
    if n % 2 == 1:
        ans = (ans + s(n // 2, l - 1) ** 2) % M
    t[(n, l)] = ans
    return ans


n, l = map(int, input().split())
r = s(n, l) - s(n, l - 1)
print(r)
