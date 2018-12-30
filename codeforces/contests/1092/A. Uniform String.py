for _ in range(int(input())):
    n, k = map(int, input().split())
    v = ord('a')
    limit = v + k
    s = ''
    for i in range(n):
        s += chr(v)
        v += 1
        if v == limit:
            v = ord('a')
    print(s)
