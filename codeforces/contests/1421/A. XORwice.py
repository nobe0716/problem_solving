def solve(a: int, b: int) -> int:
    return (a | b) - (a & b)


assert solve(6, 12) == 10
assert solve(4, 9) == 13
assert solve(59, 832) == 891

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(solve(a, b))
