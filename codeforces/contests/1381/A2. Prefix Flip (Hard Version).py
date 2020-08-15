import sys

input = sys.stdin.readline

_DEBUG = False


def flip(ch):
    return '1' if ch == '0' else '0'


def solve(n, a, b):
    if a == b:
        return [0]
    r = []

    inv_flip_count = 0
    al_idx, ar_idx = 0, n - 1

    for i in range(n - 1, -1, -1):
        if inv_flip_count % 2 == 0:
            a0, ai = a[al_idx], a[ar_idx]
        else:
            a0, ai = flip(a[al_idx]), flip(a[ar_idx])

        if ai != b[i]:
            if a0 != b[i]:
                r.append(i + 1)
            else:
                r.extend([1, i + 1])
            inv_flip_count += 1
            al_idx, ar_idx = ar_idx, al_idx

        if inv_flip_count % 2 == 0:
            ar_idx -= 1
        else:
            ar_idx += 1

    return [len(r)] + r


# assert solve(5, '01011', '11100') == [3, 1, 5, 2]

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    sys.stdout.write(' '.join(map(str, solve(n, a, b))) + '\n')
