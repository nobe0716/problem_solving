# https://codeforces.com/problemset/problem/1283/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a):
    ans = list(a)
    candidates = []
    no_receiver = []

    no_gifts = set(range(n))
    for i, e in enumerate(a):
        if e == 0:
            no_receiver.append(i)
        else:
            ans[i] = e
            no_gifts.discard(e - 1)

    no_gifts = list(sorted(no_gifts))

    cnt_empty_slot = len(no_receiver)
    for i in range(cnt_empty_slot):
        if no_receiver[i] == no_gifts[i]:
            no_receiver[i], no_receiver[(i + 1) % cnt_empty_slot] = no_receiver[(i + 1) % cnt_empty_slot], no_receiver[i]

    for i, j in zip(no_receiver, no_gifts):
        ans[i] = j + 1

    return ans


# print(solve(2 * 10 ** 5, [0] * (2 * 10 ** 5)))
n = int(input())
a = list(map(int, input().split()))
ans = solve(n, a)
print(' '.join(map(str, ans)))
