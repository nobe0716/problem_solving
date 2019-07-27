x, y, z = map(int, input().split())
a = 0
if x % z + y % z >= z:
    a = min(z - (x % z), z - (y % z))

print((x + y) // z, a)
