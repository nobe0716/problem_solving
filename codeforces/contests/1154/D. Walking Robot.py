# 2022-06-05T11:14:57Z


def proc(n, bc, ac, s):
    a, b = ac, bc

    for i in range(n):
        if a == 0 and b == 0:
            return i
        if b > 0 and s[i] == 1 and a < ac:
            b -= 1
            a += 1
        elif a == 0:
            b -= 1
        else:
            a -= 1
    return n


n, b, a = map(int, input().split())
s = list(map(int, input().split()))

ans = proc(n, b, a, s)
print(ans)
