# https://codeforces.com/problemset/problem/1263/D
# 22:13
import sys
from collections import defaultdict

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, passwords):
    g = defaultdict(set)

    # password_sets = list(map(set, passwords))\
    def translate(password):
        v = [0] * 26
        for e in password:
            v[ord(e) - ord('a')] = 1
        return v

    g = [[0] * 26 for _ in range(26)]
    for password in passwords:
        vector = translate(password)

        for i in range(26):
            if vector[i] == 1:
                g[i][i] = 1
            for j in range(i + 1, 26):
                if vector[i] == 0 or vector[j] == 0:
                    continue
                g[i][j] = g[j][i] = 1

    visited = [False] * 26
    c = 0

    for i in range(26):
        if visited[i] or g[i][i] == 0:
            continue
        c += 1
        visited[i] = True
        stack = [i]
        while stack:
            v = stack.pop()
            for j in range(26):
                if visited[j] or g[v][j] == 0:
                    continue
                visited[j] = True
                stack.append(j)
    return c


# assert solve(4, ['a', 'ac', 'b', 'cb']) == 1

n = int(input())
passwords = [input().strip() for _ in range(n)]
ans = solve(n, passwords)
print(ans)
