__author__ = 'sunghyo.jung'


n = int(input())
for i in range(n):
    s = input()
    if s == "".join(map(str, sorted(s, reverse=True))):
        print('no answer')
        continue
    idx = len(s) - 2
    while s[idx] >= s[idx + 1]:
        idx -= 1
    prefix = s[:idx]
    postfix = s[idx:]
    first_elem = None
    for elem in sorted(postfix):
        if postfix[0] < elem:
            first_elem = elem
            break
    postfix = list(postfix)
    postfix.remove(first_elem)
    res = prefix + first_elem + "".join(map(str, sorted(postfix)))
    print(res)


