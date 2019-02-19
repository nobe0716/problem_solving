for _ in range(int(input())):
    n, a, b = map(int, input().split())

    if a < b / 2:
        print(n * a)
    else:
        print((n % 2) * a + (n // 2) * b)
