import itertools

n = int(input())
s = input()

min_count = float('inf')
min_sequence = ''
for p in itertools.permutations('RGB'):
    c = 0
    sequence = list(s)
    for i in range(n):
        if p[i % 3] != s[i]:
            c += 1
            sequence[i] = p[i % 3]
    if min_count > c:
        min_count = c
        min_sequence = sequence
print(min_count)
print(''.join(min_sequence))
