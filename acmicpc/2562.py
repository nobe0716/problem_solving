a = []
mv = float('-inf')
ans = -1
for i in range(1, 10):
    v = int(input())
    a.append(v)
    if v > mv:
        mv = v
        ans = i
print(mv)
print(ans)
