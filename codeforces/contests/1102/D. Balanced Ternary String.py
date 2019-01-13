from collections import deque

n, s = int(input()), list(map(int, list(input())))
l = n // 3

pos = [deque(), deque(), deque()]
for i in range(n):
    pos[s[i]].append(i)

t = []
for i in range(3):
    t.append(l - len(pos[i]))

for i in [0, 2, 1]:
    for j in range(3):
        if i == j:
            continue
        while t[i] > 0 and t[j] < 0:
            if i < j:
                pos[i].append(pos[j].popleft())
            else:
                pos[i].append(pos[j].pop())
            t[i] -= 1
            t[j] += 1
    pos[i] = deque(list(sorted(pos[i])))
for i in range(3):
    for j in pos[i]:
        s[j] = i
print(''.join(map(str, s)))
