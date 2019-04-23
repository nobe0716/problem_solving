"""
## Name of Prob
C. Alarm Clocks Everywhere

## Link
https://codeforces.com/contest/1155/problem/C

## Note

## Input
n m
x_1 ... x_n
p_1 ... p_m

## Output

## Strategy
should see condition len of delta_values could be less than 2

"""
import math

_DEBUG = True


def solve(n, m, x, p):
    delta_values = [x[i + 1] - x[i] for i in range(n - 1)]
    delta_gcd = math.gcd(delta_values[1], delta_values[0]) if n >= 3 else delta_values[0]  # miss
    for i in range(2, n - 1):
        delta_gcd = math.gcd(delta_gcd, delta_values[i])
    for i in range(m):
        if delta_gcd % p[i] == 0:
            return min(x), i + 1
    return None


# assert solve(3, 5, [3, 12, 18], [2, 6, 5, 3, 3]) == (3, 4)
# assert solve(4, 2, [1, 5, 17, 19], [4, 5]) is None
# assert solve(4, 2, [1, 5, 17, 19], [2, 1]) == (1, 1)
# assert solve(4, 2, [1, 5, 17, 19], [2, 1]) == (1, 1)


n, m = map(int, input().split())
x = list(map(int, input().split()))
p = list(map(int, input().split()))
solution = solve(n, m, x, p)

if not solution:
    print('NO')
else:
    print('YES')
    print(solution[0], solution[1])
