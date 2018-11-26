n, k = map(int, input().split())
red, green, blue = 2 * n, 5 * n, 8 * n
print(sum(e // k + (0 if e % k == 0 else 1) for e in [red, green, blue]))
