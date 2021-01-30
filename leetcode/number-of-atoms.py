from collections import defaultdict
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from typing import Dict, Tuple


class Solution:
    def countOfAtoms(self, f: str) -> str:
        def count(i: int) -> Tuple[int, Dict[str, int]]:
            def parse_num(i: int) -> Tuple[int, int]:
                if i >= lf:
                    return i, 1
                c = 0
                while i < lf and f[i] in digits:
                    c += int(f[i])
                    c *= 10
                    i += 1
                c //= 10
                return i, c if c else 1

            d = defaultdict(int)
            while i < lf:
                if f[i] == '(':
                    i, m = count(i + 1)
                    i, c = parse_num(i)

                    for k, v in m.items():
                        d[k] += v * c
                elif f[i] in ascii_uppercase:
                    if i + 1 < lf and f[i + 1] in ascii_lowercase:
                        k = f[i: i + 2]
                        i += 2
                    else:
                        k = f[i]
                        i += 1
                    i, c = parse_num(i)
                    d[k] += c
                elif f[i] == ')':
                    return i + 1, d
            return i, d

        lf = len(f)
        i, d = count(0)
        return ''.join(k + str(v) if d[k] > 1 else k for k, v in sorted(d.items()))


s = Solution()
assert s.countOfAtoms(f="Mg(OH)2") == "H2MgO2"
assert s.countOfAtoms(f="H2O") == "H2O"
assert s.countOfAtoms(f="K4(ON(SO3)2)2") == "K4N2O14S4"
assert s.countOfAtoms(f="Be32") == "Be32"
