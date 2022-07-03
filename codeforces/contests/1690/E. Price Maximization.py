def proc(n, k, a):
    ans = 0
    na = []
    for e in a:
        ans += e // k
        na.append(e % k)

    a = sorted(na, reverse=True)

    lo, hi = 0, n - 1

    while lo < hi:
        while hi > lo and a[lo] + a[hi] < k:
            hi -= 1
        if lo == hi:
            break
        ans += 1
        lo += 1
        hi -= 1
    return ans


assert proc(6, 5, [5, 3, 8, 6, 3, 2, ]) == 5

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().strip().split()))
    ans = proc(n, k, a)
    print(ans)
