import sys


def solve(n, a):
    t = [0] * (n + 1)
    a = [0] + a
    for i in range(1, n + 1):
        if a[i] > a[i - 1]:
            t[i] = t[i - 1] + 1
        else:
            t[i] = 1
    r = 0
    for i in range(1, n + 1):
        r = max(r, t[i])
        cur_max = t[i]
        if a[i - cur_max] >= a[i - cur_max + 1] and a[i - cur_max - 1] < a[i - cur_max + 1] - 1:
            new_max = t[i - cur_max - 1] + 1 + t[i]
            r = max(r, new_max)
        elif i - cur_max + 2 <= i and a[i - cur_max] < a[i - cur_max + 2] - 1:
            new_max = t[i] + t[i - cur_max]
            r = max(r, new_max)

    return max(r, min(n, max(t) + 1))


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
r = solve(n, a)
print(r)
