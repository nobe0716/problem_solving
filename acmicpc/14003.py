import bisect
import sys

input = sys.stdin.readline

MIN_VAL = -10 ** 9 - 7
MAX_VAL = 10 ** 9 + 7


def solve(n, a):
    t = [0] * (n + 1)
    dt = [MAX_VAL] * (n + 1)
    dt[0] = MIN_VAL
    trace = [0] * n

    value2index = {}
    for i in range(n):
        e = a[i]
        idx = bisect.bisect_left(dt, e)
        t[i] = idx

        if idx > 1:
            trace[i] = value2index[dt[idx - 1]]

        dt[t[i]] = min(dt[t[i]], e)
        value2index[e] = i

    max_cnt = max(t)
    idx = value2index[dt[max_cnt]]
    history = [a[idx]]
    for i in range(max_cnt - 1):
        history.append(a[trace[idx]])
        idx = trace[idx]

    history = reversed(history)
    return max_cnt, history


# assert solve(6, [10, 20, 10, 30, 20, 50]) == (4, [10, 20, 30, 50])
n = int(input())
a = [int(x) for x in input().split()]

count, history = solve(n, a)
print(count)
print(' '.join(map(str, history)))
