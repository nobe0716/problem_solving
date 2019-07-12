a = sorted(input().split())

if a[0] == a[1] == a[2]:
    print(0)
elif (a[0][1] == a[1][1] == a[2][1]) and (int(a[0][0]) + 1 == int(a[1][0]) and int(a[1][0]) + 1 == int(a[2][0])):
    print(0)
elif a[0] == a[1] or a[1] == a[2]:
    print(1)
else:
    s = set(a)
    r = None
    for e in s:
        num, word = int(e[0]), e[1]
        if str(str(num - 2) + word) in s or str(str(num - 1) + word) in s or str(str(num + 1) + word) in s or str(
                str(num + 2) + word) in s:
            r = 1
            break
    if r:
        print(r)
    else:
        print(2)
