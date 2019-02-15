s = input()
t = input()

if len(s) != len(t):
    print('NO')
    exit(0)

vowels = set('aeiou')
for s_e, t_e in zip(s, t):
    if (s_e in vowels) ^ (t_e in vowels):
        print('NO')
        exit(0)
print('YES')