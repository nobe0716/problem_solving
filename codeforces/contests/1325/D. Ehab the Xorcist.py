def solve(u, v):
    if u == v:
        return [u]
    elif u > v:
        return None

    if (v - u) % 2 == 0:
        x = (v - u) // 2
        if u & x == 0:
            return [u | x, x]
        else:
            return [u, x, x]
    else:
        return None


# assert solve(2, 4) == [3, 1]
# assert solve(1, 3) == [1, 1, 1]
# assert solve(8, 5) is None
# assert solve(0, 0) == [0]

u, v = map(int, input().split())
r = solve(u, v)
if not r:
    print(-1)
elif u == v == 0:
    print(0)
else:
    print('{}\n{}'.format(len(r), ' '.join(map(str, r))))
