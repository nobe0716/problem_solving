# 2022-07-30T21:44:29Z


def proc(n, a):
    def get_max_sum_of_subarray(arr):
        v = arr[0]
        r = v
        for e in arr[1:]:
            v = max(e, v + e)
            r = max(r, v)
        return r

    sa = [abs(a[i] - a[i + 1]) * (-1) ** i for i in range(n - 1)]
    sb = [-e for e in sa[1:]]

    res = get_max_sum_of_subarray(sa)
    if sb:
        res = max(res, get_max_sum_of_subarray(sb))
    return res


n = int(input())
a = list(map(int, input().split()))

ans = proc(n, a)
print(ans)
