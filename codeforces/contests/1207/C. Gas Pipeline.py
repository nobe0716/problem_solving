# 2022-06-11T22:35:52.690Z

"""
suppose x consequence 0

2 * a <= (x - 1) * b

2 * a / b + 1 <= x

"""


def proc(n, a, b, s):
    if '1' not in s:
        return a * n + b * (n + 1)

    lo = 0
    hi = n - 1
    while s[lo] == '0':
        lo += 1
    while s[hi] == '0':
        hi -= 1

    cost = (n + 1) * b + (hi - lo + 2) * b + a * (n + 2)

    zero_count = 0
    for i in range(lo + 1, hi):
        if s[i] == '0':
            zero_count += 1
        elif zero_count > 0:
            if (zero_count - 1) * b > 2 * a:
                cost -= ((zero_count - 1) * b - 2 * a)
            zero_count = 0
    if zero_count > 0:
        if (zero_count - 1) * b > 2 * a:
            cost -= ((zero_count - 1) * b - 2 * a)

    return cost


assert proc(8, 2, 5, '00110010') == 94

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input()
    ans = proc(n, a, b, s)
    print(ans)
