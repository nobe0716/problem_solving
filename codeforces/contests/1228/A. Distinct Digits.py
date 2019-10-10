l, r = map(int, input().split())


def find_value(l, r):
    for i in range(l, r + 1):
        if len(set(str(i))) == len(str(i)):
            return i
    return -1


r = find_value(l, r)
print(r)
