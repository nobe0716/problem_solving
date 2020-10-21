def solve(n):
    base = [1, 11, 111, 1111]
    aparts = []
    for i in range(1, 10):
        aparts += [_ * i for _ in base]
    r = 0
    for e in aparts:
        r += len(str(e))
        if e == n:
            break
    return r


for _ in range(int(input())):
    n = int(input())
    r = solve(n)
    print(r)
