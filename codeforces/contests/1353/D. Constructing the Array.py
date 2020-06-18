import heapq

a = [0] * 2 * 10 ** 5
for _ in range(int(input())):
    n = int(input())
    h = [(-n, 0, n - 1)]

    for i in range(1, n + 1):
        v, l, r = heapq.heappop(h)
        m = (l + r) // 2
        a[m] = i
        lr, rl = m - 1, m + 1
        if l <= lr:
            heapq.heappush(h, (-(lr - l), l, lr))
        if rl <= r:
            heapq.heappush(h, (-(r - rl), rl, r))

    print(' '.join(map(str, a[:n])))
