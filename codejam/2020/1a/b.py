def solve(n):
    if n <= 31:
        return [(_, 1) for _ in range(1, n + 1)]
    n -= 31
    bin_reversed = bin(n)[2:]
    bin_reversed = '0' * (32 - len(bin_reversed)) + bin_reversed
    bin_reversed = '0' + bin_reversed[::-1]
    is_left = True
    r = []
    for i in range(1, 32):
        r.append((i, 1 if is_left else i))
        if bin_reversed[i] == '1':
            if is_left:
                for j in range(2, i + 1):
                    r.append((i, j))
            else:
                for j in range(i - 1, 0, -1):
                    r.append((i, j))
            is_left = not is_left
    for i in range(32, 32 + sum(map(int, bin_reversed))):
        r.append((i, 1 if is_left else i))
    return r


for t in range(1, int(input()) + 1):
    n = int(input())
    r = solve(n)
    print('Case #{}:'.format(t))
    for i, j in r:
        print(i, j)
