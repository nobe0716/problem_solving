from decimal import Decimal


def solve(h, c, t):
    if (h + c) / 2 >= t:
        return 2
    k = (t - h) // (h + c - 2 * t)
    # k = Decimal(k)
    # k = math.ceil(k)

    delta = lambda k: abs(Decimal((k * (h + c)) + h) / (2 * k + 1) - t)
    candidates = (k, delta(k)), (k + 1, delta(k + 1))

    return sorted(candidates, key=lambda x: x[1])[0][0] * 2 + 1


for _ in range(int(input())):
    h, c, t = map(int, input().split())
    k = solve(h, c, t)
    print(k)
