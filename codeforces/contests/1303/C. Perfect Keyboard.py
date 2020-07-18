from collections import defaultdict
from string import ascii_lowercase


def solve(tok: str):
    if len(tok) == 1:
        return ascii_lowercase
    incident_chr = defaultdict(set)

    for i in range(len(tok)):
        if i == 0:
            incident_chr[tok[i]].add(tok[i + 1])
        elif i == len(tok) - 1:
            incident_chr[tok[i]].add(tok[i - 1])
        else:
            incident_chr[tok[i]].add(tok[i + 1])
            incident_chr[tok[i]].add(tok[i - 1])

    tokens = []
    used = set()

    if any(len(incident_chr[k]) > 2 for k in incident_chr):
        return None

    for k, friends in incident_chr.items():
        if k in used:
            continue
        if len(friends) == 2:
            def gen_tok(e: str) -> str:
                used.add(e)
                l, r = list(incident_chr[e])
                v = l + e + r

                used.add(l)
                while len(incident_chr[l]) == 2:
                    ll, lr = list(incident_chr[l])
                    if ll not in used:
                        v = ll + v
                        l = ll
                    elif lr not in used:
                        v = lr + v
                        l = lr
                    else:
                        return ''
                    used.add(l)

                used.add(r)
                while len(incident_chr[r]) == 2:
                    rl, rr = list(incident_chr[r])
                    if rl not in used:
                        v = v + rl
                        r = rl
                    elif rr not in used:
                        v = v + rr
                        r = rr
                    else:
                        return ''
                    used.add(r)
                return v

            partial_value = gen_tok(k)
            if not partial_value:
                return None
            tokens.append(partial_value)
    for k, friends in incident_chr.items():
        if k in used:
            continue
        f = list(friends)[0]
        used.add(k)
        used.add(f)
        tokens.append(k + f)
    base = ''.join(tokens) if tokens else ''
    for e in ascii_lowercase:
        if e in used:
            continue
        base += e

    for i in range(len(tok)):
        if i == 0:
            if abs(base.index(tok[i]) - base.index(tok[i + 1])) > 1:
                return None
        elif i == len(tok) - 1:
            if abs(base.index(tok[i]) - base.index(tok[i - 1])) > 1:
                return None
        else:
            if abs(base.index(tok[i]) - base.index(tok[i + 1])) > 1:
                return None
            if abs(base.index(tok[i]) - base.index(tok[i - 1])) > 1:
                return None
    return base


for _ in range(int(input())):
    s = input()
    res = solve(s)
    if res:
        print('YES\n{}'.format(res))
    else:
        print('NO')
