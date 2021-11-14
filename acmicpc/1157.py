from collections import Counter

s = input()
c = Counter(s.upper())
most_common = c.most_common(2)
if len(most_common) == 1 or most_common[0][1] > most_common[1][1]:
    print(most_common[0][0])
else:
    print('?')
