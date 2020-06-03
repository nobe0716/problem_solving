def solve(a):
    length_of_side = sum(a[:3])
    return length_of_side ** 2 - (a[0] ** 2 + a[2] ** 2 + a[4] ** 2)


# assert solve([1000, 1000, 1, 1000, 1000, 1]) == 2004000
# assert solve([2, 4, 5, 3, 3, 6]) == 83
# assert solve([45, 19, 48, 18, 46, 21]) == 6099
# assert solve([1, 2, 1, 2, 1, 2]) == 13
# assert solve([1, 1, 1, 1, 1, 1]) == 6
# assert solve([7, 5, 4, 8, 4, 5]) == 175
a = list(map(int, input().split()))

r = solve(a)
print(r)
