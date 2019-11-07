from collections import Counter
import math

winner = {'R': 'P', 'S': 'R', 'P': 'S'}

R, S, P = 'R', 'S', 'P'


def solve(n, a, b, c, s):
    me = {R: a, P:b, S: c}
    opposite = Counter(s)

    if sum(min(me[winner[k]], v) for k, v in opposite.items()) < math.ceil(n / 2):
        return None

    seq = [None] * n
    for i, e in enumerate(s):
        win = winner[e]

        if me[win] > 0:
            me[win] -= 1
            seq[i] = win

    for i, e in enumerate(s):
        if not seq[i]:
            for k in me.keys():
                if me[k] > 0:
                    me[k] -= 1
                    seq[i] = k
                    break
    # print(n, a, b, c, s, seq)
    return ''.join(seq)


for _ in range(int(input())):
    n = int(input())
    a, b, c = map(int, input().split())  # R S P
    s = input()

    r = solve(n, a, b, c, s)
    if not r:
        print('NO')
    else:
        print('YES')
        print(r)
