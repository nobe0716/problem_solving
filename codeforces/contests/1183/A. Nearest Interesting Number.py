"""
## Name of Prob

## Link

## Note

## Input

## Output

## Strategy
"""

_DEBUG = True


def solve(n):
    for j in range(n, 10 ** 10):
        if sum(map(int, str(j))) % 4 == 0:
            return j
    return None


# for i in range(1, 1001):
#     r = solve(i)
#     print(i)
#     if sum(map(int, str(r))) % 4 != 0:
#         print('error', i, r)

# assert solve(432) == 435
# assert solve(98) == 103
# assert solve(99) == 103
# assert solve(237) == 237
# assert solve(42) == 44
n = int(input())
print(solve(n))
