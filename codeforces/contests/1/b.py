import re
import string

PATTERN_RC = re.compile(r'R(\d+)C(\d+)')
PATTERN_CR = re.compile(r'([A-Z]+)(\d+)')


def int_to_alpha(v):
    r = ''
    # if v <= 26:
    #     return string.ascii_uppercase[v - 1]

    while v > 0:
        v -= 1
        r += string.ascii_uppercase[v % 26]
        v //= 26
    return r[::-1]


def alpha_to_int(v):
    r = 0
    for e in v:
        r += (ord(e) - ord('A') + 1)
        r *= 26
    return r // 26


n = int(input())

for _ in range(n):
    s = input()
    m = PATTERN_RC.match(s)
    if m:
        r, c = m.group(1), int(m.group(2))
        print('{}{}'.format(int_to_alpha(c), r))
    else:
        m = PATTERN_CR.match(s)
        c, r = m.group(1), m.group(2)
        print('R{}C{}'.format(r, alpha_to_int(c)))
