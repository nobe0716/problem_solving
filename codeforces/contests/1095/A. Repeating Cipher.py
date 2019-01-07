n = int(input())
s = input()
i = 1
r = ''
while len(s) > 0:
    r += s[0]
    s = s[i:]
    i += 1
print(r)
