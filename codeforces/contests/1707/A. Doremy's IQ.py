# 2022-09-04 13:58:27.345756
# https://codeforces.com/problemset/problem/1707/A
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, q, a):
    """

    if (rest number of test) == q:
        can test all remains
    """
    initial_test_count = sum(1 if x <= q else 0 for x in a)
    if initial_test_count == n:
        return [1] * n

    def possible(v):
        test_cnt = 0
        temp_q = q
        m = [0] * n
        for i in range(v):
            if a[i] <= temp_q:
                test_cnt += 1
                m[i] = 1
        for i in range(v, n):
            if a[i] <= temp_q:
                test_cnt += 1
                m[i] = 1
            elif temp_q > 0:
                test_cnt += 1
                temp_q -= 1
                m[i] = 1
            else:
                return None

        return test_cnt, m

    lo = 0
    hi = n
    res = 0, [0] * n
    while lo <= hi:
        mid = (lo + hi) // 2
        v = possible(mid)
        if v:
            if v[0] > res[0]:
                res = v
            hi = mid - 1
        else:
            lo = mid + 1

    return res[1]


if _DEBUG:
    assert proc(2, 1, [1, 2, ]) == [1, 1]

for _ in range(int(input().strip())):
    n, q = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))

    ans = proc(n, q, a)
    print(''.join(map(str, ans)))
