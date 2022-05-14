# 2022-05-15T00:39:19.105Z
from collections import Counter


def proc(n, a):
    def check(v):
        remain_counter = Counter(a[v:])
        if len(remain_counter) == n - v:
            return True
        for i in range(v, n):
            remain_counter[a[i - v]] += 1
            if remain_counter[a[i]] == 1:
                del remain_counter[a[i]]
            else:
                remain_counter[a[i]] -= 1

            if len(remain_counter) == n - v:
                return True
        return False

    lo, hi = 0, n
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans


n = int(input())
a = list(map(int, input().split()))

print(proc(n, a))
