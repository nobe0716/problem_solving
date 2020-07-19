def get_num_of_divisors(x, a):
    if x == 1:
        return 1
    i = 2
    c = 0
    divisors = []
    while x > 1:
        while x % i == 0:
            x //= i
            c += 1

        if c > 0:
            divisors.append((i, c))
        i += 1
        c = 0

    c = 1
    for a, b in divisors:
        c *= (b + 1)
    return c


def solve(n, a):
    x = min(a) * max(a)

    return x if all(x % e == 0 for e in a) and get_num_of_divisors(x, a) - 2 == len(a) else -1


# assert solve(8, [8, 2, 12, 6, 4, 24, 16, 3]) == 48
# assert solve(1, [2]) == 4
# assert solve(13, [802, 5, 401, 4010, 62, 2, 12431, 62155, 310, 10, 31, 2005, 24862]) == -1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
