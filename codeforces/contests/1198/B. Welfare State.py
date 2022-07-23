# 2022-07-23T22:41:28Z


n = int(input())
a = list(map(int, input().split()))
q = int(input())

op1 = [(a[i], 0) for i in range(n)]
op2 = [0] * q

for i in range(q):
    s = input()
    if s[0] == '1':
        p, x = map(int, s[2:].split())
        op1[p - 1] = (x, i)
    else:
        x = int(s[2:])
        op2[i] = x

for i in range(q - 2, -1, -1):
    op2[i] = max(op2[i], op2[i + 1])

ans = [0] * n
for i in range(n):
    x, j = op1[i]
    ans[i] = max(x, op2[j])

print(' '.join(map(str, ans)))
