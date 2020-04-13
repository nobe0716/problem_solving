def solve(p):
    prefix = []
    postfix = []
    middle = []
    for e in p:
        tokens = e.split('*')
        prefix.append(tokens[0])
        postfix.append(tokens[-1])
        if len(tokens) > 2:
            middle += tokens[1:-1]

    prefix.sort(key=len, reverse=True)
    postfix.sort(key=len, reverse=True)

    if any(not prefix[0].startswith(_) for _ in prefix):
        return '*'
    if any(not postfix[0].endswith(_) for _ in postfix):
        return '*'

    return prefix[0] + ''.join(middle) + postfix[0]


for t in range(1, int(input()) + 1):
    n = int(input())
    p = [input() for _ in range(n)]
    r = solve(p)
    print('Case #{}: {}'.format(t, r))
