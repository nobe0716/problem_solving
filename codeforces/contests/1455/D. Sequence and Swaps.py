# https://codeforces.com/contest/1455/problem/D
from collections import deque, defaultdict
from typing import List

_MAX = 10 ** 9


def solve(n: int, x: int, a: List[int]) -> int:
    is_asc = [[False] * n for _ in range(n)]
    for i in range(n):
        is_asc[i][i] = True
        for j in range(i + 1, n):
            if a[j] >= a[j - 1]:
                is_asc[i][j] = True
            else:
                break
    if is_asc[0][-1]:  # already sorted
        return 0

    t = [defaultdict(lambda: _MAX) for _ in range(n)]
    for i in range(n):
        if not is_asc[0][i]:
            break
        if a[i] <= x:
            continue
        if i == 0 or x >= a[i - 1]:
            t[i][x] = 1

    for i in range(1, n):
        for j in range(i):
            x = a[j]
            if a[i] <= x:
                continue
            if i - j > 1 and not is_asc[j + 1][i - 1]:
                continue
            for k, v in t[j].items():
                if k > a[j + 1]:
                    continue
                if i - j > 1 and (not is_asc[j + 1][i - 1] or x < a[i - 1]):
                    continue
                t[i][x] = min(t[i][x], v + 1)

    res = _MAX

    for i in range(n):
        for j in t[i].keys():
            if i == n - 1 or (j <= a[i + 1] and is_asc[i + 1][-1]):
                res = min(res, t[i][j])

    if res == _MAX:
        res = -1

    # print(res)
    return res


# assert solve(56, 3, [int(x) for x in '76 21 34 81 121 84 88 115 151 139 139 149 192 178 190 317 197 202 203 207 209 216 231 270 284 287 300 301 302 303 313 454 318 326 335 340 340 341 351 355 356 368 369 371 375 375 384 391 424 451 457 467 470 479 484 488'.split()]) == 7
# assert solve(50, 1, [int(x) for x in '3 122 15 33 54 62 63 69 97 100 109 114 119 160 124 125 135 142 151 203 186 190 191 196 201 461 206 219 219 227 235 245 249 250 250 250 275 316 324 333 354 364 416 435 457 469 471 479 481 489'.split()]) == 5
# assert solve(5, 18, [int(x) for x in '81 324 218 413 324'.split()]) == 3
# assert solve(4, 1, [int(x) for x in '2 3 5 4'.split()]) == 3
# assert solve(2, 10, [11, 9]) == -1
# assert solve(5, 6, [int(x) for x in '1 1 3 4 4'.split()]) == 0
# assert solve(1, 10, [2]) == 0
# assert solve(2, 10, [12, 11]) == 1

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = deque(map(int, input().split()))

    r = solve(n, x, a)
    print(r)
