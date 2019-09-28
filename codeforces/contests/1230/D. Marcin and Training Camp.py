from collections import Counter


def solve(n, a, b):
    c = Counter(a)
    r = 0

    keys = []
    rests = []

    for ea, eb in zip(a, b):
        if c[ea] >= 2:
            keys.append(ea)
            r += eb
        else:
            rests.append((ea, eb))

    for ea, eb in rests:
        if any(k | ea == k for k in keys):
            r += eb
    return r


assert solve(10, list(map(int, '3 3 5 5 6 6 1 2 4 7'.split())), list(map(int, '1 1 1 1 1 1 1 1 1 1'.split()))) == 9
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(solve(n, a, b))
