def solve(n):
    if n == 2:
        return 2
    return n % 2


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
