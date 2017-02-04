def get_count(n, a):
    lastIndex = n - 1
    swapped = False
    cnt = 0
    for i, v in enumerate(a):
        if v - 1 - i > 2:
            return "Too chaotic"
    for i in range(lastIndex):
        for j in range(lastIndex):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                cnt += 1
                swapped = True
        if not swapped:
            break;
        swapped = False

    return cnt
for t in range(int(input())):
    print(get_count(int(input()), [int(x) for x in input().split()]))
