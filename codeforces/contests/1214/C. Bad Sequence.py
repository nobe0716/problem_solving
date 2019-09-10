n = int(input())
s = input()


def possible(n, s):
    lc = 0
    rc = 0
    for e in s:
        if e is '(':
            lc += 1
        else:
            rc += 1
        if rc - lc >= 2:
            return False
    return lc == rc


r = possible(n, s)
print('Yes' if r else 'No')
