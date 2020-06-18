def solve(n):
    if n <= 3:
        return [-1]
    BASE_CASE = [2, 4, 1, 3]

    r = []
    for i in range(0, n // 4):
        r += [x + i * 4 for x in BASE_CASE]

    if n % 4 == 1:
        # [2, 4, 1, 3, 5]
        r.append(n)
    elif n % 4 == 2:
        # [2, 4, 1, 3, 5, 6] -> [2, 4, 1, 5, 3, 6]
        v = r.pop()
        r.append(n - 1)
        r.append(v)
        r.append(n)
    elif n % 4 == 3:
        # [2, 4, 1, 3, 5, 6, 7] -> [2, 4, 1, 5, 7, 3, 6]
        v = r.pop()
        r.append(n - 2)
        r.append(n)
        r.append(v)
        r.append(n - 1)
    return r


for _ in range(int(input())):
    n = int(input())
    r = solve(n)
    print(' '.join(map(str, r)))
