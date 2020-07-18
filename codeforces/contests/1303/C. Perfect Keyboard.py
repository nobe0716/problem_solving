from string import ascii_lowercase


def solve(tok: str):
    if len(tok) == 1:
        return ascii_lowercase
    base = tok[0]
    for i in range(len(tok) - 1):
        if tok[i + 1] in base:
            if abs(base.index(tok[i]) - base.index(tok[i + 1])) > 1:
                return None
        else:
            if base.index(tok[i]) == 0:
                base = tok[i + 1] + base
            elif base.index(tok[i]) == len(base) - 1:
                base += tok[i + 1]
            else:
                return None
    base += ''.join(e for e in ascii_lowercase if e not in base)
    return base


for _ in range(int(input())):
    s = input()
    res = solve(s)
    if res:
        print('YES\n{}'.format(res))
    else:
        print('NO')
