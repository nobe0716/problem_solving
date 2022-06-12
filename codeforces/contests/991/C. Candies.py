def proc(n):
    def check(v):
        c = n
        a = 0
        while c > 0:
            if c >= v:
                c -= v
                a += v
            else:
                a += c
                c = 0
                break
            c -= (c // 10)

        return a >= (n + 1) // 2

    lo, hi = 1, (n + 1) // 2
    r = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            r = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return r


assert proc(756) == 29

n = int(input())
ans = proc(n)
print(ans)
