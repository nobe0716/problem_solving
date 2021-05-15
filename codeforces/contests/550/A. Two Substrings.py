# https://codeforces.com/contest/550/problem/A
s = input()
l = len(s)

possible = False
for lt, rt in [('AB', 'BA'), ('BA', 'AB')]:
    lo = hi = None
    for i in range(l - 1):
        if s[i] == lt[0] and s[i + 1] == lt[1]:
            lo = i
            break
    for i in range(l - 2, -1, -1):
        if s[i] == rt[0] and s[i + 1] == rt[1]:
            hi = i
            break

    if hi is not None and lo is not None and hi - lo >= 2:
        possible = True
        break

print('YES' if possible else 'NO')
