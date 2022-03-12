# 2022-03-12 20:37:27.713163
# https://codeforces.com/problemset/problem/1215/C
from collections import Counter


def proc(n, s, t):
    c = Counter(s) + Counter(t)
    if c['a'] % 2 == 1 or c['b'] % 2 == 1:
        return None

    s = list(s)
    t = list(t)

    pos = {
        'ab': [],
        'ba': [],
    }
    operations = []

    for i in range(n):
        if s[i] == t[i]:
            continue
        pos[s[i] + t[i]].append(i)

    while len(pos['ab']) >= 2:
        operations.append((pos['ab'].pop(), pos['ab'].pop()))
    while len(pos['ba']) >= 2:
        operations.append((pos['ba'].pop(), pos['ba'].pop()))

    if len(pos['ab']) == 1:
        idx_ab = pos['ab'].pop()
        idx_ba = pos['ba'].pop()
        operations.append((idx_ab, idx_ab))
        operations.append((idx_ab, idx_ba))
    return operations


n = int(input())
s = input().strip()
t = input().strip()

ans = proc(n, s, t)

if ans is None:
    print(-1)
else:
    print(len(ans))
    for e in ans:
        print('{} {}'.format(e[0] + 1, e[1] + 1))
