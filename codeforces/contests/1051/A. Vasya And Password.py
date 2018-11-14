import string

for _ in range(int(input())):
    sets = set(string.ascii_lowercase), set(string.ascii_uppercase), set(string.digits)
    s = list(input())
    cnt = [0, 0, 0]
    for c in s:
        for i in range(3):
            if c in sets[i]:
                cnt[i] += 1

    indexes = list(filter(lambda x: cnt[x] == 0, range(3)))
    if len(indexes) == 1:
        target_set = sets[indexes[0]]
        for i in range(len(s)):
            converted = False
            for j in range(3):
                if s[i] in sets[j] and cnt[j] > 1:
                    s[i] = target_set.pop()
                    converted = True
                    break
            if converted:
                break
    elif len(indexes) == 2:
        s[0] = sets[indexes[0]].pop()
        s[1] = sets[indexes[1]].pop()
    print(''.join(s))
