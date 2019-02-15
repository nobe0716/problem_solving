# import random

n = int(input())
s = input()
encoding_dict = {'R': 0, 'G': 1, 'B': 2}
s = list(map(lambda c: encoding_dict[c], s))
# n = 200000
# s = ''
# for i in range(n):
#     s += 'RGB'[random.randint(0, 2)]
MAX_VALUE = 200000
t = {c: [0] * (n + 1) for c in range(3)}
l = {c: [0] * (n + 1) for c in range(3)}
# s = ' ' + s
for i in range(1, n + 1):
    for current_ch in range(3):
        min_v = MAX_VALUE
        min_c = None
        for previous_ch in range(3):
            if current_ch == previous_ch:
                continue
            if min_v > t[previous_ch][i - 1]:
                min_v, min_c = t[previous_ch][i - 1], previous_ch
        t[current_ch][i], l[current_ch][i] = min_v, min_c
        if s[i - 1] != current_ch:
            t[current_ch][i] += 1

min_v, min_c = MAX_VALUE, None
for c in range(3):
    if min_v > t[c][n]:
        min_v, min_c = t[c][n], c
print(min_v)
r = []
for i in range(n, 0, -1):
    r.append(min_c)
    min_c = l[min_c][i]

encoding_dict = {0: 'R', 1: 'G', 2: 'B'}
print(''.join(map(lambda c: encoding_dict[c], r[::-1])))
