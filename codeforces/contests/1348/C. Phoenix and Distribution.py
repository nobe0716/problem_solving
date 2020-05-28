import sys
from collections import Counter


def solve(n, k, s):
    c = Counter(s)
    if k == 1:
        return ''.join(sorted(s))
    if len(c) == 1:
        if n % k == 0:
            return s[0] * (n // k)
        else:
            return s[0] * (n // k + 1)

    keys = list(sorted(c.keys()))
    minimum_key = keys[0]

    if c[minimum_key] == k and len(keys) == 2:
        return minimum_key + keys[1] * ((c[keys[1]] + k - 1) // k)
    elif c[minimum_key] >= k:
        return minimum_key * (c[minimum_key] - (k - 1)) + ''.join(key * c[key] for key in keys[1:])
    else:
        current_sum = 0
        for e in keys:
            current_sum += c[e]
            if current_sum >= k:
                return e


# assert solve(4, 2, 'baba') == 'ab'
# assert solve(5, 2, 'baacb') == 'abbc'
# assert solve(5, 3, 'baacb') == 'b'
# assert solve(5, 3, 'aaaaa') == 'aa'
# assert solve(6, 4, 'aaxxzz') == 'x'
# assert solve(7, 1, 'phoenix') == 'ehinopx'
# assert solve(8, 2, 'aaaaabaa') == 'aaaaaab'
r = []
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().strip().split())
    s = sys.stdin.readline().strip()
    cur = solve(n, k, s)
    r.append(cur)
    # print(cur)

sys.stdout.write('\n'.join(r))
