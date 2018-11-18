for _ in range(int(input())):
    a, b, k = map(int, input().split())
    x = 0
    if a == b:
        print(a if k % 2 == 1 else 0)
        continue
    x = (a - b) * (k // 2)
    if k % 2 == 1:
        x += a
    print(x)
