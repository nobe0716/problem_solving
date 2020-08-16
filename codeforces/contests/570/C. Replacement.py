import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = list(input())
pos = []
f0 = 0
con_pc = 0

for i in range(n):
    if s[i] == '.':
        pos.append(i)
        con_pc += 1
        if con_pc >= 2:
            f0 += 1
    else:
        con_pc = 0

r = []
for _ in range(m):
    xi, ci = input().strip().split()
    xi = int(xi) - 1

    if (s[xi] != '.' and ci == '.') or (s[xi] == '.' and ci != '.'):
        s[xi] = ci
        if ci == '.':
            if xi == 0:
                if n >= 2 and s[1] == '.':
                    f0 += 1
            elif xi == n - 1:
                if n >= 2 and s[n - 2] == '.':
                    f0 += 1
            elif n >= 3:
                if s[xi - 1] == '.' and s[xi + 1] == '.':
                    f0 += 2
                elif s[xi - 1] == '.' or s[xi + 1] == '.':
                    f0 += 1
        else:
            if xi == 0:
                if n >= 2 and s[1] == '.':
                    f0 -= 1
            elif xi == n - 1:
                if n >= 2 and s[n - 2] == '.':
                    f0 -= 1
            elif n >= 3:
                if s[xi - 1] == '.' and s[xi + 1] == '.':
                    f0 -= 2
                elif s[xi - 1] == '.' or s[xi + 1] == '.':
                    f0 -= 1
    r.append(f0)

print('\n'.join(map(str, r)))
