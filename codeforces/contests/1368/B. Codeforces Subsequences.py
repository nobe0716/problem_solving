TOKEN = 'codeforces'


def solve(n: int) -> str:
    v = 1
    counts = [1] * 10
    i = 0
    while v < n:
        v = v // counts[i] * (counts[i] + 1)
        counts[i] += 1
        i = (i + 1) % 10

    return ''.join(TOKEN[_] * counts[_] for _ in range(10))


# assert solve(1) == 'codeforces'
# assert solve(3) == 'codeforcesss'
# assert solve(10000000000000000)
n = int(input())
r = solve(n)
print(r)
