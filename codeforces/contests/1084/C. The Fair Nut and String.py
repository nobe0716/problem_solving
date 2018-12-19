MODER = 10 ** 9 + 7

s = input()
l = len(s)

tokens = []
cur_token = None
for i in range(l):
    if s[i] == 'a':
        if not cur_token:
            cur_token = [i]
        else:
            cur_token.append(i)
    elif s[i] == 'b':
        if cur_token:
            tokens.append(len(cur_token))
            cur_token = None

if cur_token:
    tokens.append(len(cur_token))

# print(tokens)
r = 0
for e in tokens:
    r = r * (e + 1) + e
    r %= MODER
print(r)
