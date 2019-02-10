"""
WIP
"""

n = int(input())
s = [input() for _ in range(2 * n - 2)]
s = sorted(s, reverse=True)
list_p = [s[0]]
list_s = []

t = ['P'] + [None] * (2 * n - 3)
big_p = list_p[0]
p_count = 1

print(s)
for i in range(1, 2 * n - 2):
    e = s[i]
    if big_p.startswith(e) and p_count < n - 1:
        t[i] = 'P'
        p_count += 1
    else:
        t[i] = 'S'
print(''.join(t))
