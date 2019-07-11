n = int(input())
a = [int(input()) for _ in range(n)]


def divide_num(num):
    index = [0, 0, 0]
    for i, divider in enumerate((2, 3, 5)):
        while num % divider == 0:
            num //= divider
            index[i] += 1
    return index if num == 1 else None


r = []
for num in a:
    index = divide_num(num)

    if index is None:
        r.append(-1)
    else:
        r.append(index[0] + index[1] * 2 + index[2] * 3)
print('\n'.join(map(str, r)))
