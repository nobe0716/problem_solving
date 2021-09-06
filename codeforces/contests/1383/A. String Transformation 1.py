# https://codeforces.com/contest/1383/problem/A
import string
import sys
from collections import defaultdict

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline

K = string.ascii_lowercase[:20]


def solve(n, a, b):
    g = defaultdict(set)
    for i in range(n):
        if a[i] > b[i]:
            return -1
        elif a[i] < b[i]:
            g[a[i]].add(b[i])
            g[b[i]].add(a[i])

    checked = {k: False for k in K}
    if _DEBUG:
        for k in sorted(g.keys()):
            print('{} -> {}'.format(k, g[k]))

    def dfs(v):
        checked[v] = True
        for n in g[v]:
            if not checked[n]:
                dfs(n)

    ans = 20
    for k in K:
        if not checked[k]:
            dfs(k)
            ans -= 1
    if _DEBUG:
        print(ans)
    return ans


assert solve(77, 'kijhomniljogijghgphipmhlmmkkkjimnmjnmlphnhnmoigoknopjgjpkompmhggkhohgolkoghhm', 'klpnppoknlojilmpkpiopommmpolpjkmoonoplphnjnppikolopponppppnpoiomnloljpnkokmpo') == 9
# assert solve(4, 'aabd', 'cccd') == 2
for _ in range(int(input().strip())):
    n = int(input().strip())
    a = input().strip()
    b = input().strip()
    ans = solve(n, a, b)
    print(ans)
