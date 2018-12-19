n = int(input())
a = [0] + list(map(int, input().split()))


def calc(x, n, a):
    return sum((2 * a[i] * (abs(x - i) + i + x - 2) for i in range(1, n + 1)))


print(min((calc(i, n, a) for i in range(1, n + 1))))
