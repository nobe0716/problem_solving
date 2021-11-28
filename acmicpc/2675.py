for _ in range(int(input())):
    r, s = input().split()
    r = int(r)
    s = ''.join(e * r for e in s)
    print(s)
