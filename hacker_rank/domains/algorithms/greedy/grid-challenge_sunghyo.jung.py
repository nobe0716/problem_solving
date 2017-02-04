__author__ = 'sunghyo.jung'
for t in range(int(input())):
    n = int(input())
    g = []
    ans = True
    for i in range(n):
        g.append(sorted(input()))
    for i in range(n - 1):
        for j in range(n):
            if g[i][j] > g[i + 1][j]:
                ans = False
                break
    print("YES" if ans else "NO")