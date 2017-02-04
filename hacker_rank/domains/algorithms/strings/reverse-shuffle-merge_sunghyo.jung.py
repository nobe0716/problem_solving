__author__ = 'sunghyo.jung'
from collections import Counter
s = raw_input()[::-1]
left = Counter(s)
need = {k: left[k] / 2 for k in left.keys()}
selected = {k: 0 for k in left.keys()}
r = []

for ch in s:
    if need[ch] == 0:
        continue
    while len(r) > 0 and ch < r[len(r) - 1] and need[r[len(r) - 1]] < left[r[len(r) - 1]]:
        need[r[len(r) - 1]] += 1
        r.pop()
    r.append(ch)
    need[ch] -= 1
    left[ch] -= 1
print "".join(r)