for _ in range(int(input())):
    l, r = map(int, input().split())
    s = 0
    if l % 2 == 0:
        if r % 2 == 1:
            s = (r - l + 1) // 2 * -1
        else:
            s = (r - l + 1) // 2 * -1 + r
    else:
        if r % 2 == 0:
            s = (r - l + 1) // 2
        else:
            s = (r - l + 1) // 2 - r
    print(s)
