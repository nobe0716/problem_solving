# 2022-03-12 14:29:48.599243
# https://codeforces.com/problemset/problem/1515/D
import sys
from collections import Counter

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, l, r, colors):
    target_match_count = n // 2
    lc = Counter(colors[:l])
    rc = Counter(colors[l:])

    for k in list(lc.keys()) if l < r else list(rc.keys()):
        ln, rn = lc[k], rc[k]

        pair_count = min(ln, rn)

        if pair_count > 0:
            target_match_count -= pair_count
            lc[k] -= pair_count
            rc[k] -= pair_count
            l -= pair_count
            r -= pair_count
            if lc[k] == 0:
                del lc[k]
            if rc[k] == 0:
                del rc[k]

    if target_match_count <= 0:
        return 0

    if l > r:
        l, r = r, l
        lc, rc = rc, lc

    if target_match_count <= l:
        return target_match_count

    operation_count = l
    target_match_count -= l
    # need to move (target_match_count - l) pairs from right to left
    rc_pair_count = sum(rc[x] // 2 for x in rc.keys())

    if rc_pair_count >= target_match_count:
        operation_count += target_match_count
        target_match_count = 0
    else:
        operation_count += rc_pair_count
        target_match_count -= rc_pair_count
    return operation_count + target_match_count * 2


# assert proc(6, 2, 4, [1, 1, 2, 2, 2, 2]) == 3

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    colors = list(map(int, input().split()))
    ans = proc(n, l, r, colors)
    print(ans)
