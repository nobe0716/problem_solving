def solve(a: int, b: int, c: int):
    maps = sorted(map(lambda x: (x % 3, x // 3), [a, b, c]))
    # print(maps)
    sum_of_quotients = sum(m[1] for m in maps)
    if maps[0][0] == 0 and maps[0][1] > 0 and maps[1][0] >= 2 and maps[2][0] >= 2:
        return sum_of_quotients + 1
    elif all(m[0] > 0 for m in maps):
        return sum_of_quotients + min(m[0] for m in maps)
    return sum_of_quotients


assert solve(3, 6, 9) == 6
assert solve(4, 4, 4) == 4
assert solve(0, 0, 0) == 0
a, b, c = map(int, input().split())
print(solve(a, b, c))
