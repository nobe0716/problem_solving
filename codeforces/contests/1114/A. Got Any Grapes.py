x, y, z = map(int, input().split())  # Andrew, Dmitry and Michal
a, b, c = map(int, input().split())  # green, purple and black grapes

a -= x
if a < 0:
    print("NO")
    exit(0)
consume = min(a, y)
a -= consume
y -= consume
consume = min(b, y)
b -= consume
y -= consume
if y > 0:
    print("NO")
    exit(0)

if a + b + c >= z:
    print("YES")
else:
    print("NO")
