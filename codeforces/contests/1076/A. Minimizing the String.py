n, s = int(input()), input()
if all(s[i] <= s[i + 1] for i in range(n - 1)):
    if n > 1:
        print(s[:-1])
    else:
        print(s)
else:
    i = list(filter(lambda i: s[i] > s[i + 1], range(n - 1)))[0]
    print(s[:i] + s[i + 1:])
