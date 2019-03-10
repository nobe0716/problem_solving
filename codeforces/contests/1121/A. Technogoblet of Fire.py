from collections import defaultdict

n, m, k = map(int, input().split())
p = [0] + list(map(int, input().split()))
s = [0] + list(map(int, input().split()))
c = list(map(int, input().split()))

max_pow = defaultdict(int)
for power_of_student, school_of_student in zip(p, s):
    max_pow[school_of_student] = max(max_pow[school_of_student], power_of_student)

r = 0
for e in c:
    if max_pow[s[e]] != p[e]:
        r += 1
print(r)
