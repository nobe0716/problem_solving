import math
import sys

input = sys.stdin.readline


def get(lo: int, hi: int) -> int:
    if lo == hi:
        return st[lo]
    elif lo > hi:
        return 1

    c = 1
    if lo % 2 == 1:
        c *= st[lo]
        lo += 1
    if hi % 2 == 0:
        c *= st[hi]
        hi -= 1
    return 0 if c == 0 else c * get(lo // 2, hi // 2)


def update(i: int, v: int):
    st[i] = 1 if v > 0 else -1 if v < 0 else 0
    i //= 2
    while i >= 1:
        new_val = st[i * 2] * st[i * 2 + 1]
        if st[i] == new_val:
            break
        st[i] = new_val
        i //= 2


st = [1] * 5 * 10 ** 5

while True:
    try:
        n, k = map(int, input().split())
        arr = [int(x) for x in input().strip().split()]
        base = 2 ** int(math.ceil(math.log2(n)))

        for i in range(n):
            st[base + i] = 1 if arr[i] > 0 else -1 if arr[i] < 0 else 0
        for i in range(n, base * 2):
            st[base + i] = 1
        for i in range(base - 1, 0, -1):
            st[i] = st[i * 2] * st[i * 2 + 1]

        ans = ''
        for _ in range(k):
            a, i, j = input().strip().split()
            i, j = int(i), int(j)
            if a == 'C':
                update(base + i - 1, j)
            else:
                v = get(base + i - 1, base + j - 1)
                if v > 0:
                    ans += '+'
                elif v < 0:
                    ans += '-'
                else:
                    ans += '0'
        print(ans)
    except:
        break
