_MODER = 10 ** 9 + 7


def solve(s):
    if 'm' in s or 'w' in s:
        return 0

    l = len(s)
    t = [[0, 0] for _ in range(l)]
    t[0][0] = 1
    for i in range(1, l):
        t[i][0] = sum(t[i - 1]) % _MODER
        if s[i - 1:i + 1] == 'uu' or s[i - 1:i + 1] == 'nn':
            t[i][1] = t[i - 1][0]

    return sum(t[l - 1]) % _MODER

s = input()
r = solve(s)
print(r)

