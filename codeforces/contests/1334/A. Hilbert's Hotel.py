def solve(n, a):
    s = set()
    for i, v in enumerate(a, start=1):
        c = (i + v) % n
        if c in s:
            return False
        s.add(c)

    return True


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    r = solve(n, a)
    print('YES' if r else 'NO')
