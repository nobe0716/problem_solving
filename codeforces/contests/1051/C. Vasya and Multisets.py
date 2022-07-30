# 2022-07-30T20:56:40Z
from collections import Counter


def proc(n, a):
    def validate(res):
        ca = Counter()
        cb = Counter()

        for ai, ri in zip(a, res):
            if ri == 'A':
                ca[ai] += 1
            else:
                cb[ai] += 1

        va = sum(1 if ca[k] == 1 else 0 for k in ca)
        vb = sum(1 if cb[k] == 1 else 0 for k in cb)
        assert va == vb

    c = Counter(a)

    unique_count = sum(1 if c[k] == 1 else 0 for k in c)

    res = [None] * n
    if unique_count % 2 == 1 and unique_count == n:
        return None

    is_a = True
    for i, e in enumerate(a):
        if c[e] > 1:
            res[i] = 'A'
        elif is_a:
            res[i] = 'A'
            is_a = not is_a
        else:
            res[i] = 'B'
            is_a = not is_a
    if unique_count % 2 == 0:
        return res
    k, v = c.most_common(n=1)[0]
    if v <= 2:
        return None
    res[a.index(k)] = 'B'
    validate(res)
    return res


# assert proc(100, list(map(int,
#                           '9 9 72 55 14 8 55 58 35 67 3 18 73 92 41 49 15 60 18 66 9 26 97 47 43 88 71 97 19 34 48 96 79 53 8 24 69 49 12 23 77 12 21 88 66 9 29 13 61 69 54 77 41 13 4 68 37 74 7 6 29 76 55 72 89 4 78 27 29 82 18 83 12 4 32 69 89 85 66 13 92 54 38 5 26 56 17 55 29 4 17 39 29 94 3 67 85 98 21 14'.split()))) is not None

n = int(input())
a = list(map(int, input().split()))

ans = proc(n, a)
if ans:
    print('YES')
    print(''.join(ans))
else:
    print('NO')
