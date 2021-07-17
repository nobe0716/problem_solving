# https://codeforces.com/contest/1497/problem/C2


def simple(n: int):
    if n % 2 == 1:
        return [1, n // 2, n // 2]
    elif n % 4 == 0:
        return [n // 4, n // 4, n // 2]
    else:
        return [2, n // 2 - 1, n // 2 - 1]


def solve(n: int, k: int):
    return [1] * (k - 3) + simple(n - (k - 3))


for _ in range(int(input())):
    n, k = map(int, input().split())
    r = solve(n, k)
    print(' '.join(map(str, r)))
