# 2022-10-15T16:42:08.327Z
import sys

sys.setrecursionlimit(501)


def proc(n, l, r, s):
    num_base = (r - l + 1)

    # cur_sum = sum(base)
    candidate_value = n
    diff = s
    base = [None] * num_base
    for i in range(len(base)):
        budget = (num_base - i) * (num_base - i - 1) // 2
        if diff - budget < 1:
            return None
        if candidate_value <= diff - budget:
            base[i] = candidate_value
            candidate_value -= 1
        else:
            base[i] = diff - budget
        diff -= base[i]
    if sum(base) != s or len(set(base)) != len(base):
        return None

    rest_numbers = set(range(1, n + 1)).difference(set(base))
    res = [None] * (n + 1)
    res[l:r + 1] = list(base)

    j = 1
    for i in range(1, l):
        while j not in rest_numbers:
            j += 1
        rest_numbers.discard(j)
        res[i] = j
    for i in range(r + 1, n + 1):
        while j not in rest_numbers:
            j += 1
        rest_numbers.discard(j)
        res[i] = j
    return res


# assert proc(2, 1, 1, 1) is not None
# assert proc(1, 1, 1, 1) == [None, 1]

for _ in range(int(input())):
    n, l, r, s = map(int, input().split())
    ans = proc(n, l, r, s)
    if ans:
        print(' '.join(map(str, ans[1:])))
    else:
        print(-1)
