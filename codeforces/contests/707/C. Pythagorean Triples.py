# https://codeforces.com/problemset/problem/707/C


def solve(n):
    if n <= 2:
        return -1

    mul = 1
    cnt = 0
    while n % 2 == 0:
        n //= 2
        mul *= 2
        cnt += 1

    if n != 1:
        a = n ** 2 // 2
        b = a + 1
    else:
        a = 3
        b = 5
        if mul >= 4:
            mul //= 4

    a *= mul
    b *= mul
    return '{} {}'.format(a, b)


n = int(input())
ans = solve(n)
print(ans)
