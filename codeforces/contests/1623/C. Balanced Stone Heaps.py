# 2022-07-09T14:36:30Z


def proc(n, a):
    def check(mid):
        for i in range(n):
            t[i] = a[i]
        for i in range(n - 1, 1, -1):
            if t[i] < mid:
                return False
            d = min(a[i], t[i] - mid) // 3
            t[i - 1] += d
            t[i - 2] += 2 * d
        return t[0] >= mid and t[1] >= mid

    lo, hi = 1, max(a)
    t = [0] * n
    res = 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res


assert proc(4, [1, 2, 10, 100]) == 7

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split()))

    print(proc(n, a))
