from collections import Counter

n = int(input())
s = input()
c = Counter(s)
if c['1'] != c['0']:
    print(1)
    print(s)
else:
    print(2)
    print(s[0], s[1:])
